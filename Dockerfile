FROM nfcore/base:1.8
LABEL authors="Bilge Sürün" \
      description="Docker image containing all software requirements for the KohlbacherLab/nextflow-clinvap pipeline"

# Install the conda environment
COPY environment.yml /
RUN conda env create -f /environment.yml && conda clean -a

# Add conda installation dir to PATH (instead of doing 'conda activate')
ENV PATH /opt/conda/envs/nextflow-clinvap-1.0dev/bin:$PATH

# Dump the details of the installed packages to a file for posterity
RUN conda env export --name nextflow-clinvap-1.0dev > nextflow-clinvap-1.0dev.yml
