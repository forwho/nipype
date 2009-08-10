"""Provide interface classed to AFNI commands."""
__docformat__ = 'restructuredtext'


from nipype.interfaces.base import Bunch, CommandLine


class To3d(CommandLine):
    """ `To3d` converts ...

    This is an afni program

    Examples
    --------
    >>> to3d = afni.To3d(anat=True)
    >>> to3d.inputs.datum = 'float'
    >>> to3d.run()
    
    """

    @property
    def cmd(self):
        """Base command for To3d"""
        return 'to3d'

    def inputs_help(self):
        doc = """
          Optional Parameters
          -------------------
        """
        print doc

    def _populate_inputs(self):
        """Initialize the inputs attribute."""
        self.inputs = Bunch(infiles=None,
                            anat=None,
                            datum=None,
                            session=None,
                            prefix=None,
                            epan=None,
                            skip_outliers=None,
                            assume_dicom_mosaic=None,
                            time=None,
                            )

    def _parseinputs(self):
        """Parse valid input options for To3d command.

        Ignore options set to None.

        """


        out_inputs = []
        inputs = {}
        [inputs.update({k:v}) for k, v in self.inputs.iteritems() \
             if v is not None]
        for opt in inputs:
            if opt is 'infiles':
                pass # placeholder to suppress not supported warning
            elif opt is 'anat':
                out_inputs.append('-anat')
            elif opt is 'datum':
                out_inputs.append('-datum %s' % inputs[opt])
            elif opt is 'session':
                out_inputs.append('-session %s' % inputs[opt])
            elif opt is 'prefix':
                out_inputs.append('-prefix %s' % inputs[opt])
            elif opt is 'epan':
                out_inputs.append('-epan')
            elif opt is 'skip_outliers':
                out_inputs.append('-skip_outliers')
            elif opt is 'assume_dicom_mosaic':
                out_inputs.append('-assume_dicom_mosaic')
            elif opt is 'time':
                # -time:zt nz nt TR tpattern  OR  -time:tz nt nz TR tpattern
                # time : list
                #    zt nz nt TR tpattern
                #    tz nt nz TR tpattern
                if len(inputs[opt]) != 5:
                    raise ValueError('time requires five parameters')
                slice_order = inputs[opt][0]
                cmd = '-time:%s' % slice_order
                if slice_order == 'zt':
                    nz = int(inputs[opt][1])
                    nt = int(inputs[opt][2])
                    cmd += ' %d %d' % (nz, nt)
                elif slice_order == 'tz':
                    nt = int(inputs[opt][1])
                    nz = int(inputs[opt][2])
                    cmd += ' %d %d' % (nt, nz)
                else:
                    raise ValueError('Invalid slice input order!')
                TR = float(inputs[opt][3])
                tpattern = inputs[opt][4]
                cmd += ' %f %s' % (TR, tpattern)
                out_inputs.append(cmd)
            else:
                print '%s: option %s is not supported!' % (
                    self.__class__.__name__, opt)

        # Handle positional arguments independently
        if self.inputs['infiles']:
            out_inputs.append('%s' % self.inputs['infiles'])

        return out_inputs

    def _compile_command(self):
        """Generate the command line string from the list of arguments."""
        valid_inputs = self._parseinputs()
        allargs =  [self.cmd] + valid_inputs
        self.cmdline = ' '.join(allargs)


class Threedrefit(CommandLine):
    """
    """

    @property
    def cmd(self):
        """Base command for Threedrefit"""
        return '3drefit'

    def inputs_help(self):
        doc = """
          Optional Parameters
          -------------------
        """
        print doc

    def _populate_inputs(self):
        """Initialize the inputs attribute."""
        self.inputs = Bunch(deoblique=None,
                            xorigin=None,
                            yorigin=None,
                            zorigin=None,
                            infile=None)

    def _parseinputs(self):
        """Parse valid input options for Threedrefit command.

        Ignore options set to None.

        """

        out_inputs = []
        inputs = {}
        [inputs.update({k:v}) for k, v in self.inputs.iteritems() \
             if v is not None]
        for opt in inputs:
            if opt is 'deoblique':
                out_inputs.append('-deoblique')
            elif opt is 'xorigin':
                out_inputs.append('-xorigin %s' % inputs[opt])
            elif opt is 'yorigin':
                out_inputs.append('-yorigin %s' % inputs[opt])
            elif opt is 'zorigin':
                out_inputs.append('-zorigin %s' % inputs[opt])
            elif opt is 'infile':
                pass # placeholder to suppress not supported warning
            else:
                print '%s: option %s is not supported!' % (
                    self.__class__.__name__, opt)

        # Handle positional arguments independently
        if self.inputs['infile']:
            out_inputs.append('%s' % self.inputs['infile'])

        return out_inputs

    def _compile_command(self):
        """Generate the command line string from the list of arguments."""
        valid_inputs = self._parseinputs()
        allargs =  [self.cmd] + valid_inputs
        self.cmdline = ' '.join(allargs)


class Threedresample(CommandLine):
    """
    """

    @property
    def cmd(self):
        """Base command for Threedresample"""
        return '3dresample'

    def inputs_help(self):
        doc = """
          Optional Parameters
          -------------------
        """
        print doc

    def _populate_inputs(self):
        """Initialize the inputs attribute."""
        self.inputs = Bunch(orient=None,
                            outfile=None,
                            infile=None)

    def _parseinputs(self):
        """Parse valid input options for Threedrefit command.

        Ignore options set to None.

        """

        out_inputs = []
        inputs = {}
        [inputs.update({k:v}) for k, v in self.inputs.iteritems() \
             if v is not None]

        if inputs.has_key('orient'):
	    val = inputs.pop('orient')
            out_inputs.append('-orient %s' % val)
	if inputs.has_key('outfile'):
	    val = inputs.pop('outfile')
            out_inputs.append('-outfile %s' % val)
	if inputs.has_key('infile'):
	    val = inputs.pop('infile')
            out_inputs.append('-infile %s' % val)

	if len(inputs) > 0:
            print '%s: unsupported options: %s' % (
                self.__class__.__name__, inputs.keys())


        return out_inputs

    def _compile_command(self):
        """Generate the command line string from the list of arguments."""
        valid_inputs = self._parseinputs()
        allargs =  [self.cmd] + valid_inputs
        self.cmdline = ' '.join(allargs)
