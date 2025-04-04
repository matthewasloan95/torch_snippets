"""View statistics of tensors and other python containers"""

# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/inspector.ipynb.

# %% auto 0
__all__ = ["inspect"]

# %% ../nbs/inspector.ipynb 2
from .loader import *
from .registry import AttrDict
import torch


# %% ../nbs/inspector.ipynb 3
def inspect(*arrays, **kwargs):
    """
    shows shape, min, max and mean of an array/list/dict of oreys
    Usage:
    inspect(arr1, arr2, arr3, [arr4,arr5,arr6], arr7, [arr8, arr9],...)
    where every `arr` is  assume to have a .shape, .min, .max and .mean methods
    """
    depth = kwargs.pop("depth", 0)
    names = kwargs.pop("names", None)

    if names is not None:
        if "," in names:
            names = names.split(",")
        assert len(names) == len(
            arrays
        ), "Give as many names as there are tensors to inspect"
    if depth == 0:
        line()
    for ix, arr in enumerate(arrays):
        name = "\t" * depth
        name = (
            name + f"{names[ix].upper().strip()}:\n" + name
            if names is not None
            else name
        )
        name = name
        typ = type(arr).__name__

        if isinstance(arr, AttrDict) and (AttrDict not in kwargs.get("suppress", [])):
            arr = arr.to_dict()
            inspect(arr, depth=depth + 1, **kwargs)

        elif isinstance(arr, (L, list, tuple)):
            print(f"{name}{typ} of {len(arr)} items")
            inspect(*arr[: kwargs.get("max_items", 5)], depth=depth + 1, **kwargs)
            if len(arr) > kwargs.get("max_items", 5):
                print(
                    "\t" * (depth + 1)
                    + f"and ... ... {len(arr) - kwargs.get('max_items', 5)} more item(s)"
                )

        elif (
            isinstance(arr, dict) and (dict not in kwargs.get("suppress", []))
        ) or hasattr(arr, "dict"):
            if hasattr(arr, "dict"):
                arr = dcopy(arr).dict()
            print(f"{name}{typ} of {len(arr)} items")
            for ix, (k, v) in enumerate(arr.items()):
                inspect(v, depth=depth + 1, names=[k])
                if ix == kwargs.get("max_items", 5) - 1:
                    break

            if len(arr) > kwargs.get("max_items", 5):
                print(
                    "\t" * (depth)
                    + f"... ... {len(arr) - kwargs.get('max_items', 5)} more item(s)"
                )

        elif isinstance(arr, pd.DataFrame):
            print(f"{name}{typ}\tShape: {arr.shape}")

        elif isinstance(arr, BB):
            info = f"{name}{typ}\t{arr}"

        elif hasattr(arr, "shape"):
            if isinstance(arr, torch.Tensor):
                info = arr
            else:
                sh, m, M, dtype = arr.shape, arr.min(), arr.max(), arr.dtype
                try:
                    me = arr.mean()
                except:
                    me = arr.float().mean()
                info = f"{name}{typ}\tShape: {sh}\tMin: {m:.3f}\tMax: {M:.3f}\tMean: {me:.3f}\tdtype: {dtype}"
                if hasattr(arr, "device"):
                    info += f" @ {arr.device}"
            print(info)

        elif isinstance(arr, str):
            if len(arr) > 50:
                arr = arr[:25] + "..." + arr[-25:]
            print(f"{name}{typ} `{arr}`")
        else:
            try:
                ln = len(arr)
                print(f"{name}{typ} Length: {ln}")
            except:
                print(f"{name}{typ}: {arr}")
        if depth == 0:
            line()
