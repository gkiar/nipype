# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from nipype.testing import assert_equal
from nipype.interfaces.ants.utils import JacobianDeterminant

def test_JacobianDeterminant_inputs():
    input_map = dict(args=dict(argstr='%s',
    ),
    dimension=dict(argstr='%d',
    mandatory=True,
    position=0,
    usedefault=False,
    ),
    environ=dict(nohash=True,
    usedefault=True,
    ),
    ignore_exception=dict(nohash=True,
    usedefault=True,
    ),
    norm_by_total=dict(argstr='%d',
    position=5,
    ),
    num_threads=dict(nohash=True,
    usedefault=True,
    ),
    output_prefix=dict(argstr='%s',
    genfile=True,
    hash_files=False,
    position=2,
    ),
    projection_vector=dict(argstr='%s',
    position=6,
    sep='x',
    ),
    template_mask=dict(argstr='%s',
    position=4,
    ),
    terminal_output=dict(nohash=True,
    ),
    use_log=dict(argstr='%d',
    position=3,
    ),
    warp_file=dict(argstr='%s',
    mandatory=True,
    position=1,
    ),
    )
    inputs = JacobianDeterminant.input_spec()

    for key, metadata in input_map.items():
        for metakey, value in metadata.items():
            yield assert_equal, getattr(inputs.traits()[key], metakey), value

def test_JacobianDeterminant_outputs():
    output_map = dict(jacobian_image=dict(),
    )
    outputs = JacobianDeterminant.output_spec()

    for key, metadata in output_map.items():
        for metakey, value in metadata.items():
            yield assert_equal, getattr(outputs.traits()[key], metakey), value
