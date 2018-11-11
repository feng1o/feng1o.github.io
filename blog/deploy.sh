#!/bin/bash

echo "--> clean"
hexo clean

echo "--> generate"
hexo g

echo "--> deploy"
hexo d
