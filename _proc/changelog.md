# Changelog
#### 0.546
✨ `printfile` will act like `cat` for linux
✨ `choose` will let you know what was chosen
✨ `Timer` can accept `N=None` and it will simply time the current activities without any estimate
✨ `tryy` is pickleable (helps with multiprocessing)

#### 0.546
🎉 Add profiler

#### 0.545
🎉 environment variable `AD_SHOW_FULL_STRINGS` can be set to non-empty to show full strings in summary
🎉 better integration for unknown datatypes in `AD.summary`

#### 0.544
🎉 Quality of life improvements in logging
🎉 Add support for `dataclass` in `AD`
🎉 DeepDiff integrated into `AD`. Now you can call x.diff(y) where x is `AD` and y is `AD`able
🎉 `AD.d` (no brackets, d is a property) to convert the object to dictionary
✨ `read_json` can also do json.loads if input is not a file path
✨ `json` is loaded by default on import *

#### 0.540
✨ Made all imports lazy for a faster import experience

#### 0.539
✨ set `AD_SHOW_TAB_STOPS` env variable to anything to print with tab-stops (only recommended to see on REPL. Default is good for storing files)
✨ `crop_from_bb` has `padding` (px,py,pX,pY)
🐞 minor bugfix in `AD`
🎉 `AD` has a `fetch2` which preserves json structure while fetching all the leafs of the same name
🎉 `AD` has a `flatten` which flattens all nested jsons into flat dictionary with '.' combined key names
🎉 `AD` has a `flatten_and_make_dataframe` which creates one column for each nesting
✨ `tryy` will store all its errors and can be accessed by calling `<func>.error_summary()`
🎉 torch snippets as a new cli function called `ts`, thanks to the wonderful `Typer`. Try 
  `ts time` 
  `ts zen-of python` 
  `ts zen-of c++`
  `ts --help`

#### 0.538.1
✨ slightly better error printing in `tryy`

#### 0.538
🎉 `tryy` a new decorator to wrap try except with optional default return as well as print stack trace if need be
✨ `Timer` can given time-remaning approximation based on both instantaneous or average speed
✨ `logging_mode` functions can be used as both context managers and decorators
✨ better formatting for `now()`
✨ `show` auto generates a title if possible
✨ `show` function includes a `framecount` parameter to specify which frame of the stack it should search for the title. See its usage in `show_big_dataframe`
✨ `yolo_2_df` and `df_2_yolo` functions in adapters

#### 0.537
✨ `AD` let's you know if a collection is list, set or tuple
✨ NEW DEFAULT: use `info` column to show text else `text`
🐞 fix a bug where `P` misbehaves in `AD` when it doesn't exist
🐞 fix a bug in `show` tables
🐞 `logger_mode` context will gracefully exit
✨ `to` is compatible with `transformers.BatchFeature`
⏮️ Revert back `P` as the code is incompatible with py312

#### 0.536
🆕 `parse`ing a .ini file will add a `META` key by default which has `file` and `name` information. This header can be used in the file variables without creating META to begin with
🆕 `parse` will merge a base config if a `META.base` key is found. Works recursively on base files (base of base etc...)
🆕 `P` can tab complete existing file path name and access that file as an attribute
💡 Did you know parse can perform arithmetic?
✨ `registry` and `parse` are imported by default
✨ `jitter` can work on `pd.DataFrame` directly
🔨 `bbs2df` clips negative coordinates
✨ Using 🏷️ to denote data-type in `AD`
🐞 `AD2` is `AD` now
🐞 `AD` preserves dict order during serialization
✨ `warn_on_fail` decorator gives you a free try catch
✨ `show`ing a dataframe of the correct format inside and outside jupyter environments
🐞 `AD` has improved `get`, `update`, `map` and new `write_config`, `trymap` and `__json__`
✨ `P` has two new properties `.sz` for size of file and `.tree` to print the tree

#### 0.535
🐞 `AD` hotfix

#### 0.534
🎉 `store_scrap` is a new way to store on disk and show jupyter cell outputs in other notebooks.  
Best for presenting complex analyses without worrying about running time-consuming notebooks
🎉 Add support for `P` in AD `summary` and `write_json`
🎉 `__json__` supports custom objects' serializability
🎉 `write_json` is compatible with above feature
🎉 `AD_MAX_ITEMS` if given as -1 will change it to 1000
🐞 `iou` will parse input dataframes more gracefully
🐞 `AD` minor bug fix
🎉 `tree` has a better default
🎉 New functions `folder_structure_to_dict` and `folder_structure_to_json` in `paths`
🎉 Add `jitter` (int) argument to `show` so that bounding boxes can be a bit jittered
🎉 Add support for changing `spinner` in `notify_waiting`
🎉 `dumpdill` can print a custom message (see `store_scrap` in paths.py)


#### 0.531
🎉 AD `__contains__` can do a nested `in` 'x.y.z' in AD(x={'y': {'z': 10}}) == True

#### 0.530
☠️ Stop using rich's print and revert back to builtin print
🐞 Decouple AD and torch
🎉 Add a new chart - spider / radar
🎉 Add scp client with download upload functionality

#### 0.529
🧹 change code to remove future warnings in text_utils

#### 0.528
🐞 AD string summary was buggy

#### 0.524
🐞 all write modes are 'a' by default to avoid accidental overwriting
🧹 AD writes better string summary (support for multiline)

#### 0.523
🧹 `print_module_ios_for` has better targeted functionality where you need to give submodules name
🎉 `clean_gpu_mem` and `get_latest_checkpoint` functions in torch_loader
🧹 `minor bugfix in AD`

#### 0.522
🐞 minor bugfix in `AD2` where data keyword misbehaves
🧹 `video` has better size functionality
🎉 `if all is given in print_ios_for_module, all modules are printed`
🎉 `AD2.dict` is an alias for `AD2.to_dict`
🎉 better `AD2.summary` for pandas dataframes and `AD2.summary` respects max_items for keys as well
🎉 new alias `pd.read_pqt` for `pd.read_parquet`
🐞 wrap `tree` into python

#### 0.521

🐞 `read` loads color image by default
🧹 `video` utils are present in torch_snippets.video

#### 0.520

🧹 Back to min python version 3.7

#### 0.519

🎉 `print_folder_summary`

#### 0.518

🧹 import `AD` from markup2 by default
🎉 pandas dataframe summary in AD.summary

#### 0.517

🐞 `print_shapes_hook` will gracefully fail

#### 0.516

🐞 `attach` will add hook to the input module as well (not just the children)

#### 0.514

🐞 minor change in `print_shapes_hook`

#### 0.513

🎉 print_module_io_for automates attaching and detaching hooks
🎉 AD2 avoids rich printing

#### 0.512

🐞 `attach_hooks` will accept any custom hook

#### 0.511

🎉 Make `markup2.AD.__repr__` the summary
🎉 Expose `markup2.AD` as `AD2`
🎉 Make `icecream` a requirement
🎉 Min python is 3.8

#### 0.510

🎉 New IO hooks system in `torch_snippets.trainer.hooks`
🎉 Updated markup2.AD.summary and add print_summary methods

#### 0.509

🎉 Experimental `AD` in torch_snippets.markup2 that infers variable names E.g. - `(p=10; AD(p) == {'p': 10})`
🐞 `isin` will not add +1 (useful for both absolute and relative boxes now)
🐞 `write_json` will support numpy, torch and AttrDict

#### 0.508

🎉 add `find_address` to `AttrDict` that can return all path locations for a specific key
🎉 add `summary` to `AttrDict` that can give an outline of the dictionary
🎉 add `write_summary` to `AttrDict` that writes the summary to a textfile
🎉 `show` can now show bb colors `{"r": (255, 0, 0), "g": (0, 255, 0), "b": (0, 0, 255), "y": (255, 0, 255)}` if `df` has column called `color`
🎉 `AD` is an alias for `AttrDict`
🎉 `AD` can directly consume kwargs

#### 0.507

🧹 import only important functins from `dates.py`
🎉 add `backup_all_notebooks` that backs up every notebook present in a specific folder
🎉 `reset_logger` can disable stdout logging if needed, using `disable_stdout=True` kwarg (False by default)
`common_items` will take a list of folders and return common stems from the folders
images will show a black border when grid is True

#### 0.506

Info, Debug, Warn and Excep will format ouputs separated by a `;` when args are passed
`notify_waiting` is a new function that letting you know some process is running for an unknown amount of time
optional `delay` during `shutdown_current_notebook`
Info, Debug, Warn and Excep will all have `X_mode` and `in_X_mode` functions much like in_debug_mode and debug_mode
`__init__` will auto pull from logger now
Better non-linear `Timer` (and `Report` and `track2`)

#### 0.505

🧹 `Info`, `Debug`, `Warn` and `Excep` will accept args (instead of a single arg)
🧹 `show` will show h4 headers instead of h2 for dataframe titles

#### 0.504

🧹 `phasify` loads by default
🧹 `show_big_dataframe` can show more rows
🎉 add a new submodule `trainer.hooks`
🧹 `show` delegated kwargs to `plt.imshow` for a better readme
🎉 `batchify` can batchify multiple containers at once
🎉 `cat_with_padding` new function in `torch_loader`
🧹 `L` is json compatible
🐞 `BB` will not decide if something is relative/absolute
🎉 `__contains__` for config
🎉 `to` works on `AttrDict`
👶🏼 `track2` is a better version of `track` uses corouties
👶🏼 `debug_mode` temporarily activates `DEBUG` mode on
👶🏼 `if in_debug_mode():` lets you know if `DEBUG` mode is on
🧹 `reset_logger` can accept lowercase levels also
🧹 `dumpdill` will return a Path after dumping

#### 0.503

bugfix in `loader.show`
add `today` function to dates
add `are_equal_dates` to dates
add dpi option to pdf

#### 0.502

bugfix in attrdict.map

#### 0.500

All notebooks are formatted with black
`parse` can parse python expressions
Add DeepLearningConfig class that can be used to load model hyperparameters
Add GenericConfig class that can be used to load generic (such as training, evaluation) hyperparameters
Add date utilities
`patch_to`, `Timer`, `timeit`, `io` are loaded by default
`lovely_tensors` is optional
Add phasify function to loader

#### 0.499.29

attrdict can deserialize "L"

#### 0.499.28

- `show` can render a dataframe with a title
- `show` can accept a csv file as input (no need to load it and send)
- `backup_this_notebook` will back up as `backups/file/file__0000.html` instead of `backups/file/0000.html` for easier sharability
- module loads `decorators` by default (`io`, `timeit`, `check_kwargs_not_none`)
- `ishow` is less opinionated
- `shutdown_this_notebook` is a new function

## Todo

override_previous_backup should not trigger when there's no backup to begin with
instead of showing markdown objects using display, directly show HTML objects so that the text is preserved on reopen h2 in Backup instead of h1
