# Zonal Statistics for Multiband Rasters - QGIS plugin

QGIS 3 plugin that extends Zonal Statistics by running on all bands of a
multiband raster in one go.

Useful with rasters of features extracted for supervised classification or
hyperspectral raster images.


## Install

### Add plugins repository

To install this plugin, you need to add our QGIS Repository first.  Go to
`Plugins -> Manage and Install Plugins`.

On the Settings tab, enable `Show also experimental plugins`, and add a
repository named `Dymaxion Labs` with the following URL:

```
https://dymaxionlabs.github.io/qgis-repository/plugins.xml
```

After that, press `Reload all repositories` button to load our plugins index
into QGIS.


### Install plugin

Finally, go to `Plugins -> Manage and Install Plugins`, and in `All` or `Not
Installed` tabs, search for *Zonal Statistics for Multiband Rasters*.  Click
`Install plugin`.


## Usage

This is a *processing plugin*, you will have to enable the Processing Toolbox
on QGIS to use it properly.


## Issue tracker

Please report any bugs and enhancement ideas using the GitHub issue tracker:

  https://github.com/dymaxionlabs/qgis-zonal-statistics-multiband/issues

Feel free to also ask questions on our [Gitter
channel](https://gitter.im/dymaxionlabs/qgis-zonal-statistics-multiband), or by email.


## Help wanted

Any help in testing, development, documentation and other tasks is highly
appreciated and useful to the project.

For more details, see the file [CONTRIBUTING.md](CONTRIBUTING.md).


## License

Source code is released under a GNU GPL v3 license.  Please refer to
[LICENSE.md](LICENSE.md) for more information.
