#!/bin/bash

# make common dir and link js files in common to the new local common dir
mkdir -p ./chucksite/js/common && ln ./../../common/src/main/js/react/* ./chucksite/js/common && ln ./../../common/src/main/js/common.js ./chucksite/js/common