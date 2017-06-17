# Inside Core ML

This is a Python script that lets you look inside your Core ML **.mlmodel** files. Useful for troubleshooting and to satisfy the curious mind.

To use it:

```
python3 lookieloo.py name.mlmodel
```

This will print a bunch of information about your model to stdout.

Requirements:

- Python 3
- protobuf

**NOTE:** You will want to tweak the script to suit your own model. Right now it only prints information for models that are neural network classifiers (like Inception-v3). If you use a different type of model, you'll need to look at different fields.

The mlmodel spec is written in protobuf, so to learn more about the possible fields in your model you should check out the [Core ML model specification](https://docs-assets.developer.apple.com/coreml/documentation/mlmodel_specification.zip). For example, the possible fields for a convolution layer are documented in NeuralNetwork.proto, under `ConvolutionLayerParams`. 

To see your entire model, enable the line:

```python
print(model)
```

If you do this you should really pipe the output from the script to a file because it will include all the weights, so this is going to be a big data dump:

```
python3 lookieloo.py name.mlmodel > ~/Desktop/out.txt
```

The current version of this script is made for **coremltools 0.3.0**. If you have a later version of coremltools, you will need to regenerate the **_pb2.py** files. Here's how to do this:

- [Download the latest Core ML model specification](https://docs-assets.developer.apple.com/coreml/documentation/mlmodel_specification.zip)
- From the mlmodel_specification folder, run the following command:

```
protoc --python_out=/path/to/InsideCoreML *.proto
```

Links: [coremltools](https://pypi.python.org/pypi/coremltools)
