#! /bin/bash
THEME="Adwaita-Slim"

cd Compiled

for variant in '' '-dark'; do
  cd $THEME${variant}
  tar -czf $THEME${variant}.tar.gz *
  mv $THEME${variant}.tar.gz ../..
  cd ..
done
