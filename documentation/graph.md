# Table of Contents
 - [graph](#graph): Generate a 2d graph with given x and y values.
 - [pie_chart](#pie_chart): Generate a pie chart by supplying a list of labels and values.
 - [plot_gas_dens](#plot_gas_dens)
 - [star_scatter_plot](#star_scatter_plot): Generate a scatter plot by supplying a list of x, y, and z values.

## graph

### Description:
Generate a 2d graph with given x and y values.


### Parameters:


| Name | Type | Description | Default |
| --- | --- | --- | --- |
| labels | list |         The list of labels. | required |
| values | list |         The list of values. | required |

## pie_chart

### Description:
Generate a pie chart by supplying a list of labels and values.


### Parameters:


| Name | Type | Description | Default |
| --- | --- | --- | --- |
| labels | list |         The list of labels. | required |
| values | list |         The list of values. | required |

## plot_gas_dens

## star_scatter_plot

### Description:
Generate a scatter plot by supplying a list of x, y, and z values.


### Parameters:


| Name | Type | Description | Default |
| --- | --- | --- | --- |
| x | list |         The list of x values. | required |
| y | list |         The list of y values. | required |
| z | list |         The list of z values. | required |
| parts | list |         list of values (like form.scalar factor) associated with each star | required |
| whole | number |         the whole number to compare to each part | required |
