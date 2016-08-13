import sass

sass.compile(
    dirname=('site/static/scss', 'site/static/css'),
    output_style='compressed',
)
