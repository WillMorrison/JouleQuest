load("@my_deps//:requirements.bzl", "requirement")
load("@rules_python//python:defs.bzl", "py_binary")

py_binary(
    name = "smoketest",
    srcs = ["smoketest.py"],
    deps = [
        requirement("pygame"),
        requirement("pygame_gui"),
    ],
)
