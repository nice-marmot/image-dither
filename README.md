# image_dithering

Dithering is a class of methods that apply noise/distortions to a set of data to minimize quantization error.

This is intended to highlight differences and effectiveness of different dithering methods, not necessarily to replicate the original image. Dithering is done with a 5-color greyscale color palette unless otherwise specified. While the below dithering methods work for color images as well, I'm keeping them to greyscale for the moment to keep comparisons to luminance and texture.

## Original image:
![Original image](outputs/original.jpg)

## Greyscale image:
Values in original image mapped to greyscale by luminance. This is used as the input for each dithering algorithm. 
![Greyscale image](outputs/greyscale.png)

## Closest value mapping:
This method is not dithering, but rather a simple mapping of each greyscale pixel to one of five colors (white -> 3 shades of Grey -> Black). This is sort of a worst-case dithering application, as much of the details in the original image are lost, there is very visible color banding, etc. Essentially, this is what happens when the number of colors in the image is reduced with little finesse. Dithering attempts to reproduce the details of the original image, while still only needing a small set of base colors.
![Floyd-Steinberg](outputs/closest_value.png)

## Floyd-steinberg dithering:
This process also maps pixels in the full greyscale image to values in the palette, but has the added feature of propegating errors to adjacent pixels. This allows the outputted image to approximate values outside of the palette by mixing values in the palette. While the below image is clearly still quite distorted compared to the original greyscale, it is a much better approximation than simply mapping each pixel to the closest value available in the palette. A few good illustrations are the gradient caused by the mist surrounding the mountaintop and the reflections of the trees along the shoreline. These details are ill-resolved in the closest value mapping, but are decently approximated here while using the exact same colors, just applied more intelligently.
![Floyd-Steinberg](outputs/floyd_steinberg.png)

## Ordered dithering
Ordered dithering selects each pixel's value via a texture map based on a Bayer matrix. This matrix adds a pattern of offsets across the whole image applied over an nxn pixel area. This example uses an 8x8 [bayer matrix](https://en.wikipedia.org/wiki/Ordered_dithering), meaning the pattern is applied in 64-pixel squares across the whole image. A characteristic of this dithering method is the hatching patterns that it creates in many areas of the image (see the zoomed-in image below). For this particular image, this method does a good job or replicating the gradients in the water close to the camera, as well as some of the tree reflections along the shore line.
![Ordered dithering](outputs/ordered_dithering.png)
![Ordered dithering closeup](outputs/ordered_dithering_zoom.png)
