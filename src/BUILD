load("@pip//:requirements.bzl", "requirement")
load("@rules_python//python:defs.bzl", "py_library")

py_library(
    name = "main",
    srcs = ["main.py"],
    deps = [
        ":generator_ui",
        ":generator_model",
        requirement("pygame"),
        requirement("pygame_gui"),
    ],
    visibility=["//visibility:public"]
)

py_library(
    name = "generator_model",
    srcs = ["generator_model.py"],
    deps = [
        ":component",
        ":output_component_mixins",
    ]
)

py_library(
    name = "generator_ui",
    srcs = ["generator_ui.py"],
    deps = [
        "@rules_python//python/runfiles",
        requirement("pygame"),
        requirement("pygame_gui"),
    ],
    data = [
        "//assets:images/light_switch_off_256x256.png",
        "//assets:images/light_switch_on_256x256.png"
    ],
)

py_library(
    name = "component",
    srcs = ["component.py"],
)

py_test(
    name = "component_test",
    srcs = ["component_test.py"],
    deps = [
        ":component",
    ],
    size = "small",
)

py_library(
    name = "output_component_mixins",
    srcs = ["output_component_mixins.py"],
    deps = [
        ":component",
    ]
)

py_test(
    name = "output_component_mixins_test",
    srcs = ["output_component_mixins_test.py"],
    deps = [
        ":component",
        ":output_component_mixins",
    ],
    size = "small",
)
