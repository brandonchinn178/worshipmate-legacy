module.exports = function (grunt) {
    grunt.loadNpmTasks("grunt-contrib-sass");
    grunt.loadNpmTasks("grunt-contrib-watch");

    grunt.initConfig({
        sass: {
            dist: {
                options: {
                    style: 'compressed'
                },
                files: [{
                    expand: true,
                    cwd: "site/static/scss",
                    src: "**/*.scss",
                    dest: "site/static/css",
                    ext: ".css"
                }]
            }
        },
        watch: {
            sass: {
                files: "site/static/scss/**/*.scss",
                tasks: "sass"
            }
        }
    });

    grunt.registerTask("build", ["sass"]);
    grunt.registerTask("default", ["build", "watch"]);
};