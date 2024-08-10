import torch as t
print(t.__version__)

x = t.tensor([[2.0,3.0],[4.0,5.0]],requires_grad=True)
print(x)
y = x.sum()
y.backward()
print(x.grad)