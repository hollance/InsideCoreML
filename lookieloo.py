import os
import sys
import Model_pb2

args = sys.argv[1:]
if len(args) != 1:
    print("usage: %s name.mlmodel" % os.path.basename(__file__))
    exit(-1)
model_path = args[0]

model = Model_pb2.Model()

print("Loading model...")
f = open(model_path, "rb")
model.ParseFromString(f.read())
f.close()

print(model.description)

print("\nLayers:")
for layer in model.neuralNetworkClassifier.layers:
    print(layer.name)
    if layer.HasField("convolution"):
        print("\tis convolution")
        print("\tkernel size:", layer.convolution.kernelSize)
        print("\tinput channels", layer.convolution.kernelChannels)
        print("\toutput channels", layer.convolution.outputChannels)

print("\nPreprocessing:")
print(model.neuralNetworkClassifier.preprocessing)

# Enable this to see the whole thing. Warning: it will also print all the weights!
#print(model)
