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
    },
    "TRUFFLE-API" : {
      "path" : "lib/truffle-api.jar",
      "urls" : "",
      "maven" : {
        "groupId" : "com.oracle.truffle",
        "artifactId" : "truffle-api",
        "version" : "0.13"
      },
      "sha1" : "1591f730dbc7df76819c4d2f84ebc2a060fcc3a6"
    },
    "TRUFFLE-DSL" : {
      "path" : "lib/truffle-dsl-processor.jar",
      "urls" : "",
      "maven" : {
        "groupId" : "com.oracle.truffle",
        "artifactId" : "truffle-dsl-processor",
        "version" : "0.13"
      },
      "sha1" : "45890a4c28db129d76a774925525670d5b610208"
    }
  },

  "projects" : {
    "sampleproj" : {
      "sourceDirs" : ["src"],
      "dependencies" : [
       "JODA",
       "TRUFFLE-API",
      ],
      "javaCompliance" : "1.8",
      "annotationProcessors" : ["TRUFFLE-API", "TRUFFLE-DSL"]
    }
  },

  "distributions" : {
    "SAMPLE" : {
      "path" : "build/sample.jar",
      "mainClass" : "sample.RunJodaDemo",
      "dependencies" : ["sampleproj"],
      "exclude" : [
        "JODA",
        "TRUFFLE-API",
      ],
      "annotation_processors" : "",
      "addClassPath" : True
    }
  }
}
