# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ..preprocess import TCorrelate


def test_TCorrelate_inputs():
    input_map = dict(args=dict(argstr='%s',
    ),
    environ=dict(nohash=True,
    usedefault=True,
    ),
    ignore_exception=dict(nohash=True,
    usedefault=True,
    ),
    out_file=dict(argstr='-prefix %s',
    name_source='xset',
    name_template='%s_tcorr',
    ),
    outputtype=dict(),
    pearson=dict(argstr='-pearson',
    ),
    polort=dict(argstr='-polort %d',
    ),
    terminal_output=dict(nohash=True,
    ),
    xset=dict(argstr='%s',
    copyfile=False,
    mandatory=True,
    position=-2,
    ),
    yset=dict(argstr='%s',
    copyfile=False,
    mandatory=True,
    position=-1,
    ),
    )
    inputs = TCorrelate.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_TCorrelate_outputs():
    output_map = dict(out_file=dict(),
    )
    outputs = TCorrelate.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
