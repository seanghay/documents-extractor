
```shell
docker run -it --rm \
  -v $PWD/photos:/workspace/photos \
  -v $PWD/result:/workspace/result \
  ghcr.io/seanghay/documents-extractor:main
```