
**Clinical Variant Annotation Pipeline**.


[![Nextflow](https://img.shields.io/badge/nextflow-%E2%89%A519.10.0-brightgreen.svg)](https://www.nextflow.io/)
[![install with bioconda](https://img.shields.io/badge/install%20with-bioconda-brightgreen.svg)](http://bioconda.github.io/)
[![Docker](https://img.shields.io/docker/automated/nfcore/clinvap.svg)](https://hub.docker.com/r/nfcore/clinvap)

## Introduction

The pipeline is created via [`nf-core template`](https://nf-co.re/) and built using [Nextflow](https://www.nextflow.io), a workflow tool to run tasks across multiple compute infrastructures in a very portable manner. It comes with docker containers making installation trivial and results highly reproducible.

## Quick Start

i. Install [`nextflow`](https://nf-co.re/usage/installation)

ii. Install one of [`docker`](https://docs.docker.com/engine/installation/), [`singularity`](https://www.sylabs.io/guides/3.0/user-guide/) or [`conda`](https://conda.io/miniconda.html)

iii. Download the pipeline and test it on a minimal dataset with a single command

```bash
nextflow run KohlbacherLab/nextflow-clinvap -profile test,<docker/singularity/conda/institute>
```

> Please check [nf-core/configs](https://github.com/nf-core/configs#documentation) to see if a custom config file to run nf-core pipelines already exists for your Institute. If so, you can simply use `-profile institute` in your command. This will enable either `docker` or `singularity` and set the appropriate execution settings for your local compute environment.

iv. Start running your own analysis!

<!-- TODO nf-core: Update the default command above used to run the pipeline -->

```bash
nextflow run KohlbacherLab/nextflow-clinvap -profile <docker/singularity/conda/institute> --annotated_vcf <input> --skip_vep true
```

See [usage docs](docs/usage.md) for all of the available options when running the pipeline.

## Documentation

The KohlbacherLab/nextflow-clinvap pipeline comes with documentation about the pipeline, found in the `docs/` directory:

1. [Installation](https://nf-co.re/usage/installation)
2. Pipeline configuration
    * [Local installation](https://nf-co.re/usage/local_installation)
    * [Adding your own system config](https://nf-co.re/usage/adding_own_config)
    * [Reference genomes](https://nf-co.re/usage/reference_genomes)
3. [Running the pipeline](docs/usage.md)
4. [Output and how to interpret the results](docs/output.md)
5. [Troubleshooting](https://nf-co.re/usage/troubleshooting)

<!-- TODO nf-core: Add a brief overview of what the pipeline does and how it works -->

## Credits

KohlbacherLab/nextflow-clinvap was originally written by Bilge Sürün. It is created using [nf-core](https://nf-co.re/) pipeline template. 

## Contributions and Support

If you would like to contribute to this pipeline, please see the [contributing guidelines](.github/CONTRIBUTING.md).

For further information or help, don't hesitate to get in touch on [Slack](https://nfcore.slack.com/channels/clinvap) (you can join with [this invite](https://nf-co.re/join/slack)).

## Citation

<!-- TODO nf-core: Add citation for pipeline after first release. Uncomment lines below and update Zenodo doi. -->
If you use  KohlbacherLab/nextflow-clinvap for your analysis, please cite the following article:

> Sürün, B., Schärfe, C.P., Divine, M.R., Heinrich, J., Toussaint, N.C., Zimmermann, L., Beha, J. and Kohlbacher, O., 2020. ClinVAP: a reporting strategy from variants to therapeutic options. Bioinformatics, 36(7), pp.2316-2317. [https://doi.org/10.1093/bioinformatics/btz924](https://doi.org/10.1093/bioinformatics/btz924) 
