import os
import argparse
import yaml
from jinja2 import Environment, FileSystemLoader


def get_render_name(template_file: str) -> str:
    """
    This function splits a filename to remove the extension.

    Args:
        template_file (str): Filename.

    Returns:
        str: A filename without the extension.
    """
    return template_file.split(".")[0]


def render_template(yaml_file: str, template_data):
    """
    This function renders a template file using jinja

    Args:
        template_data: Parsed YAML object.
        yaml_file (str): File Path for variable yaml
    """
    with open(yaml_file, "r", -1, "utf-8") as yaml_variables:
        params = yaml.safe_load(yaml_variables)

    env = Environment(loader=FileSystemLoader("."))
    template = env.get_template(template_data["path"])

    # Render template with parameters
    output = template.render(params)

    basename = os.path.basename(template_data["path"])
    config_name = get_render_name(basename) + "." + template_data["extension"]
    # Write the rendered config to a file
    with open(f"./rendered/{config_name}", "w", -1, "utf-8") as config:
        config.write(output)

    print(f"{config_name} has been generated.")


def main():
    parser = argparse.ArgumentParser(
        description="Render a Jinja2 template with YAML parameters."
    )
    parser.add_argument(
        "-y",
        "--yaml",
        required=True,
        help="Path to the YAML file (e.g. app.yml)",
    )
    parser.add_argument(
        "-t",
        "--templates",
        required=True,
        help="Path to the templates yaml file",
    )
    args = parser.parse_args()

    with open(args.templates, "r", -1, "utf-8") as templates_yml:
        templates = yaml.safe_load(templates_yml)

    for template in templates:
        render_template(args.yaml, template)


if __name__ == "__main__":
    main()
