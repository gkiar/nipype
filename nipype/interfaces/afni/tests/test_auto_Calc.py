# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from nipype.testing import assert_equal
from nipype.interfaces.afni.preprocess import Calc

def test_Calc_inputs():
    input_map = dict(args=dict(argstr='%s',
    ),
    environ=dict(nohash=True,
    usedefault=True,
    ),
    expr=dict(argstr='-expr "%s"',
    mandatory=True,
    position=3,
    ),
    ignore_exception=dict(nohash=True,
    usedefault=True,
    ),
    in_file_a=dict(argstr='-a %s',
    mandatory=True,
    position=0,
    ),
    in_file_b=dict(argstr=' -b %s',
    position=1,
    ),
    in_file_c=dict(argstr=' -c %s',
    position=2,
    ),
    other=dict(argstr='',
    ),
    out_file=dict(argstr='-prefix %s',
    name_source='in_file_a',
    name_template='%s_calc',
    ),
    outputtype=dict(),
    single_idx=dict(),
    start_idx=dict(requires=['stop_idx'],
    ),
    stop_idx=dict(requires=['start_idx'],
    ),
    terminal_output=dict(nohash=True,
    ),
    )
    inputs = Calc.input_spec()

    for key, metadata in input_map.items():
        for metakey, value in metadata.items():
            yield assert_equal, getattr(inputs.traits()[key], metakey), value

def test_Calc_outputs():
    output_map = dict(out_file=dict(),
    )
    outputs = Calc.output_spec()

    for key, metadata in output_map.items():
        for metakey, value in metadata.items():
            yield assert_equal, getattr(outputs.traits()[key], metakey), value
