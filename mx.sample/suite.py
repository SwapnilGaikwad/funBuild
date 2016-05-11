suite = {
  "mxversion" : "5.19.6",
  "name" : "samplesuite",
  "javac.lint.overrides" : "none",

  "libraries" : {
    "JODA" : {
      "path" : "lib/joda-time-2.9.3.jar",
      "urls" : [ "http://central.maven.org/maven2/joda-time/joda-time/2.9.3/joda-time-2.9.3.jar" ],
      "maven" : {
        "groupId" : "joda-time",
        "artifactId" : "joda-time",
        "version" : "2.9.3"
      },
      "sha1" : "9e46be514a4ed60bcfbaaba88a3c668cf30476ab"
    }
  },

  "projects" : {
    "sampleproj" : {
      "sourceDirs" : ["src"],
      "dependencies" : [
       "JODA",
       "mx:JUNIT"
      ],
      "javaCompliance" : "1.8"
    }
  },

  "distributions" : {
    "SAMPLE" : {
      "path" : "build/sample.jar",
      "mainClass" : "sample.RunJodaDemo",
      "dependencies" : ["sampleproj"],
      "exclude" : [
        "JODA",
        "mx:JUNIT"
      ]
    }
  }
}
