FROM frolvlad/alpine-glibc:alpine-3.8_glibc-2.28

LABEL maintainer 'sshojiro'

RUN apk update && \
    apk --no-cache add bash ca-certificates wget libxext libxrender libstdc++ && \
    update-ca-certificates && \
    apk --update add tzdata && \
    cp /usr/share/zoneinfo/Asia/Tokyo /etc/localtime && \
    apk del tzdata

RUN echo 'export PATH=/opt/anaconda/bin:$PATH' > /etc/profile.d/anaconda.sh && \
    wget --quiet https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/anaconda.sh && \
    /bin/bash ~/anaconda.sh -b -p /opt/anaconda && \
    rm ~/anaconda.sh

ENV PATH /opt/anaconda/bin:$PATH 

RUN conda install joblib=0.14.1 networkx=2.4 numpy=1.18.1 \
                  pandas=0.25.3 python=3.7.0 scikit-learn=0.22.1 \
                  scipy=1.4.1 && \ 
    conda install -c rdkit rdkit=2019.09.3.0 && \
    conda install -c conda-forge pymatgen=2019.12.3 && \
    pip install --upgrade pip && \ 
    pip install jupyter==1.0.0 matplotlib==3.1.3 tqdm==4.42.1
