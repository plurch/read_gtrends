Google Trends Reader
========

Description
--------

This module reads and parses a [Google Trends](http://www.google.com/trends/) CSV file and returns a [Pandas](http://pandas.pydata.org/) time series object.

The resulting time series object can be used for plotting and data analysis.

Requirements
--------

This module is compatible with Python 2.7+/3.3+.

Dependencies
--------

[Pandas](http://pandas.pydata.org/) 0.13+

[dateutil](https://labix.org/python-dateutil) 2.1+

Usage
--------

Example:

    > from read_gtrends import read_gtrends
    > my_series = read_gtrends.read_gtrends('path/to/report.csv')
    > test.head()
        2004-01-04    44
        2004-01-05    44
        2004-01-06    44
        2004-01-07    44
        2004-01-08    44
        dtype: int64
    > type(my_series)
        pandas.core.series.Series


