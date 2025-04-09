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


def render_template(yaml_file, template_file):
    with open(yaml_file, "r", -1, "utf-8") as yaml_variables:
        params = yaml.safe_load(yaml_variables)

    env = Environment(loader=FileSystemLoader("."))
    template = env.get_template(template_file)

    # Render template with parameters
    output = template.render(params)
    
    config_name = get_render_name(template_file) + ".conf"
    # Write the rendered config to a file
    with open(config_name, "w", -1, "utf-8") as config:
        config.write(output)

    print("nginx.conf has been generated.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Render a Jinja2 template with YAML parameters."
    )
    parser.add_argument(
        "-y", "--yaml", required=True, help="Path to the YAML file (e.g. app.yml)"
    )
    parser.add_argument(
        "-t",
        "--template",
        required=True,
        help="Path to the Jinja2 template file (e.g. nginx.jinja)",
    )

    args = parser.parse_args()

    render_template(args.yaml, args.template)
