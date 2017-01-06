#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block
# Generated: Sat Aug 20 17:13:44 2016
##################################################

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from gnuradio import analog
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import uhd
from gnuradio import wxgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.wxgui import forms
from gnuradio.wxgui import scopesink2
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import time
import wx


class top_block(grc_wxgui.top_block_gui):

    def __init__(self):
        grc_wxgui.top_block_gui.__init__(self, title="Top Block")
        _icon_path = "/usr/share/icons/hicolor/32x32/apps/gnuradio-grc.png"
        self.SetIcon(wx.Icon(_icon_path, wx.BITMAP_TYPE_ANY))

        ##################################################
        # Variables
        ##################################################
        self.variable_text_box_0 = variable_text_box_0 = 0
        self.variable_slider_1 = variable_slider_1 = 0.1e6
        self.samp_rate = samp_rate = 10e6
        self.amp = amp = 0.1

        ##################################################
        # Blocks
        ##################################################
        _variable_slider_1_sizer = wx.BoxSizer(wx.VERTICAL)
        self._variable_slider_1_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_variable_slider_1_sizer,
        	value=self.variable_slider_1,
        	callback=self.set_variable_slider_1,
        	label="Frecuencia",
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._variable_slider_1_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_variable_slider_1_sizer,
        	value=self.variable_slider_1,
        	callback=self.set_variable_slider_1,
        	minimum=50e3,
        	maximum=10e6,
        	num_steps=1000,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_variable_slider_1_sizer)
        _amp_sizer = wx.BoxSizer(wx.VERTICAL)
        self._amp_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_amp_sizer,
        	value=self.amp,
        	callback=self.set_amp,
        	label='amp',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._amp_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_amp_sizer,
        	value=self.amp,
        	callback=self.set_amp,
        	minimum=0.1,
        	maximum=1,
        	num_steps=1000,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_amp_sizer)
        self.wxgui_scopesink2_0 = scopesink2.scope_sink_c(
        	self.GetWin(),
        	title="Scope Plot",
        	sample_rate=samp_rate,
        	v_scale=0,
        	v_offset=0,
        	t_scale=0,
        	ac_couple=False,
        	xy_mode=False,
        	num_inputs=1,
        	trig_mode=wxgui.TRIG_MODE_AUTO,
        	y_axis_label="Counts",
        )
        self.Add(self.wxgui_scopesink2_0.win)
        self._variable_text_box_0_text_box = forms.text_box(
        	parent=self.GetWin(),
        	value=self.variable_text_box_0,
        	callback=self.set_variable_text_box_0,
        	label='variable_text_box_0',
        	converter=forms.float_converter(),
        )
        self.Add(self._variable_text_box_0_text_box)
        self.uhd_usrp_sink_0 = uhd.usrp_sink(
        	",".join(("", "")),
        	uhd.stream_args(
        		cpu_format="fc32",
        		channels=range(1),
        	),
        )
        self.uhd_usrp_sink_0.set_samp_rate(samp_rate)
        self.uhd_usrp_sink_0.set_center_freq(0, 0)
        self.uhd_usrp_sink_0.set_gain(0, 0)
        self.uhd_usrp_sink_0.set_antenna("TX/RX", 0)
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vff((amp, ))
        self.blocks_float_to_complex_0 = blocks.float_to_complex(1)
        self.blocks_delay_0 = blocks.delay(gr.sizeof_float*1, int(samp_rate/variable_slider_1/2))
        self.analog_sig_source_x_0 = analog.sig_source_f(samp_rate, analog.GR_SIN_WAVE, variable_slider_1, 1, 0)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_multiply_const_vxx_0, 0))    
        self.connect((self.blocks_delay_0, 0), (self.blocks_float_to_complex_0, 1))    
        self.connect((self.blocks_float_to_complex_0, 0), (self.uhd_usrp_sink_0, 0))    
        self.connect((self.blocks_float_to_complex_0, 0), (self.wxgui_scopesink2_0, 0))    
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.blocks_delay_0, 0))    
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.blocks_float_to_complex_0, 0))    

    def get_variable_text_box_0(self):
        return self.variable_text_box_0

    def set_variable_text_box_0(self, variable_text_box_0):
        self.variable_text_box_0 = variable_text_box_0
        self._variable_text_box_0_text_box.set_value(self.variable_text_box_0)

    def get_variable_slider_1(self):
        return self.variable_slider_1

    def set_variable_slider_1(self, variable_slider_1):
        self.variable_slider_1 = variable_slider_1
        self.analog_sig_source_x_0.set_frequency(self.variable_slider_1)
        self.blocks_delay_0.set_dly(int(self.samp_rate/self.variable_slider_1/2))
        self._variable_slider_1_slider.set_value(self.variable_slider_1)
        self._variable_slider_1_text_box.set_value(self.variable_slider_1)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.uhd_usrp_sink_0.set_samp_rate(self.samp_rate)
        self.wxgui_scopesink2_0.set_sample_rate(self.samp_rate)
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)
        self.blocks_delay_0.set_dly(int(self.samp_rate/self.variable_slider_1/2))

    def get_amp(self):
        return self.amp

    def set_amp(self, amp):
        self.amp = amp
        self._amp_slider.set_value(self.amp)
        self._amp_text_box.set_value(self.amp)
        self.blocks_multiply_const_vxx_0.set_k((self.amp, ))


def main(top_block_cls=top_block, options=None):

    tb = top_block_cls()
    tb.Start(True)
    tb.Wait()


if __name__ == '__main__':
    main()
