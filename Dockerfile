FROM python:2.7.18

WORKDIR /app

# Install Sass
RUN curl -fsSL https://github.com/sass/dart-sass/releases/download/1.54.5/dart-sass-1.54.5-linux-x64.tar.gz \
        | tar xzf - --strip-components=1 -C /usr/local/bin dart-sass/sass

# Install Python requirements
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

# Compile Sass files
RUN sass site/static/scss:site/static/css --style=compressed

EXPOSE 8080
ENTRYPOINT ["bin/entrypoint.sh"]
