/* global module */
'use strict';

module.exports = function (grunt) {
  grunt.registerTask('style', function () {
    grunt.task.run([
      'sass:dist',
      'postcss'//,
      //'csslint'
    ]);
  });
};
