# Contributing to Our Projects, Version 1.0

**NOTE: This CONTRIBUTING.md is for software contributions. You do not need to follow the Developer's Certificate of Origin (DCO) process for commenting on the 192 Support Squadron repository documentation, such as CONTRIBUTING.md, INTENT.md, etc. or for submitting issues.**

Thanks for thinking about using or contributing to this software ("Project") and its documentation!

- [Policy & Legal Info](#policy)
- [Getting Started](#getting-started)
- [Submitting an Issue](#submitting-an-issue)
- [Submitting Code](#submitting-code)

## Policy

### 1. Introduction

The project maintainer for this Project will only accept contributions using the Developer's Certificate of Origin 1.1 located at [developercertificate.org](https://developercertificate.org) ("DCO"). The DCO is a legally binding statement asserting that you are the creator of your contribution, or that you otherwise have the authority to distribute the contribution, and that you are intentionally making the contribution available under the license associated with the Project ("License").

### 2. Developer Certificate of Origin Process

Before submitting contributing code to this repository for the first time, you'll need to sign a Developer Certificate of Origin (DCO) (see below). To agree to the DCO, add your name and email address to the [CONTRIBUTORS.md](https://github.com/192-Support-Squadron/nginix-letsencrypt-proxy/blob/master/CONTRIBUTORS.md) file. At a high level, adding your information to this file tells us that you have the right to submit the work you're contributing and indicates that you consent to our treating the contribution in a way consistent with the license associated with this software (as described in [LICENSE.md](https://github.com/192-Support-Squadron/nginix-letsencrypt-proxy/blob/master/LICENSE.md)) and its documentation ("Project").

### 3. Important Points

Pseudonymous or anonymous contributions are permissible, but you must be reachable at the email address provided in the Signed-off-by line.

If your contribution is significant, you are also welcome to add your name and copyright date to the source file header.

U.S. Federal law prevents the government from accepting gratuitous services unless certain conditions are met. By submitting a pull request, you acknowledge that your services are offered without expectation of payment and that you expressly waive any future pay claims against the U.S. Federal government related to your contribution.

If you are a U.S. Federal government employee and use a `*.mil` or `*.gov` email address, we interpret your Signed-off-by to mean that the contribution was created in whole or in part by you and that your contribution is not subject to copyright protections.

### 4. DCO Text

The full text of the DCO is included below and is available online at [developercertificate.org](https://developercertificate.org):

```txt
Developer Certificate of Origin
Version 1.1

Copyright (C) 2004, 2006 The Linux Foundation and its contributors.
1 Letterman Drive
Suite D4700
San Francisco, CA, 94129

Everyone is permitted to copy and distribute verbatim copies of this
license document, but changing it is not allowed.

Developer's Certificate of Origin 1.1

By making a contribution to this project, I certify that:

(a) The contribution was created in whole or in part by me and I
    have the right to submit it under the open source license
    indicated in the file; or

(b) The contribution is based upon previous work that, to the best
    of my knowledge, is covered under an appropriate open source
    license and I have the right under that license to submit that
    work with modifications, whether created in whole or in part
    by me, under the same open source license (unless I am
    permitted to submit under a different license), as indicated
    in the file; or

(c) The contribution was provided directly to me by some other
    person who certified (a), (b) or (c) and I have not modified
    it.

(d) I understand and agree that this project and the contribution
    are public and that a record of the contribution (including all
    personal information I submit with it, including my sign-off) is
    maintained indefinitely and may be redistributed consistent with
    this project or the open source license(s) involved.
```

## Getting Started

nginix-letsencrypt-proxy uses jinja to generate a nginx config, docker compose and kickstarter script to enable a TLS enabled reverse proxy for a backend application. Please feel free to submit changes.

## Submitting an Issue

You should feel free to [submit an issue](https://github.com/192-Support-Squadron/nginix-letsencrypt-proxy/issues) on our GitHub repository for anything you find that needs attention on the website. That includes content, functionality, design, or anything else!

### Submitting a Bug Report

When submitting a bug report on the website, please be sure to include accurate and thorough information about the problem you're observing. Be sure to include:

- Steps to reproduce the problem,
- What you expected to happen,
- What actually happend (or didn't happen), and
- Technical details including your Operating System name and version and Web browser name and version number.

## Submitting Code

When making your changes, it is highly encouraged that you use a [branch in Git](https://git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Merging), then submit a [pull request](https://github.com/192-support-squadron/nginix-letsencrypt-proxy/pulls) (PR) on GitHub. Your pull request will go through some automated checks using [Github Actions](https://github.com/features/actions), a continuous integration and deployment tool.

After review by the 192 Support Squadron, your PR will either be commented on with a request for more information or changes, or it will be merged into the `dev` branch.

Assuming everything checks out, the 192 Support Squadron will merge the `dev` branch into the `main` branch which will automatically publish the package to NPM.
