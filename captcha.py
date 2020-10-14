#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 15:33:39 2020

@author: venky
"""
from  PIL  import  Image , ImageDraw , ImageFont , ImageFilter
import  string
import  random

class  Captcha ():
    '''
    captcha_size: captcha image size
    font_size: font size
    text_number: the number of characters in the verification code
    line_number: number of lines
    background_color: background color of the verification code
    sources: sampling character set. The characters in the verification code are randomly selected from this
    save_format: Verification code save format
    '''
    def  __init__ ( self , captcha_size = ( 150 , 100 ), font_size = 30 , text_number = 4 , line_number = 4 , background_color = ( 255 , 255 , 255 ), sources = None , save_format = 'png' ):
        self . text_number  =  text_number
        self . line_number  =  line_number
        self . captcha_size  =  captcha_size
        self . background_color  =  background_color
        self . font_size  =  font_size
        self . format  =  save_format
        if  sources :
            self . sources  =  sources
        else :
            self . sources  =  string . ascii_letters  +  string . digits

    def  get_text ( self ):
        text  =  random . sample ( self . sources , k = self . text_number )
        return  '' . join ( text )

    def  get_font_color ( self ):
        font_color  = ( random . randint ( 0 , 150 ), random . randint ( 0 , 150 ), random . randint ( 0 , 150 ))
        return  font_color

    def  get_line_color ( self ):
        line_color  = ( random . randint ( 0 , 250 ), random . randint ( 0 , 255 ), random . randint ( 0 , 250 ))
        return  line_color

    def  draw_text ( self , draw , text , font , captcha_width , captcha_height , spacing = 20 ):
        '''
        Draw the incoming characters on the picture
        :param draw: brush object
        :param text: all characters drawn
        :param font: font object
        :param captcha_width: the width of the captcha
        :param captcha_height: the height of the captcha
        :param spacing: the gap between each character
        :return:
        '''
        # Get the height and width of this string of characters
        text_width , text_height  =  font . getsize ( text )
        # Get the approximate width of each font
        every_value_width  =  int ( text_width  /  4 )

        # The total length of this string of characters
        text_length  =  len ( text )
        
        # There is a gap between every two characters, get the total gap
        total_spacing  = ( text_length - 1 ) *  spacing

        IF  total_spacing  +  text_width  >=  captcha_width:
            raise  ValueError ( "The font plus the gap exceeds the width of the image!" )

        # Get the first character drawing position
        start_width  =  int (( captcha_width  -  text_width  -  total_spacing ) /  2 )
        start_height  =  int (( captcha_height  -  text_height ) /  2 )

        # Draw each character in turn
        for  value  in  text :
            position  =  start_width , start_height
            print ( position )
            # Draw text
            draw . text ( position , value , font = font , fill = self . get_font_color ())
            # Change the starting position of the next character
            start_width  =  start_width  +  every_value_width  +  spacing

    DEF  draw_line ( Self , Draw , captcha_width , captcha_height ):
        '''
        Draw lines
        :param draw: brush object
        :param captcha_width: the width of the captcha
        :param captcha_height: the height of the captcha
        :return:
        '''
        # Randomly get the coordinates of the starting position
        the begin  = ( Random . the randint ( 0 , captcha_width / 2 ), Random . the randint ( 0 , captcha_height ))
        # Randomly get the coordinates of the end position
        End  = ( Random . the randint ( captcha_width / 2 , captcha_width ), Random . the randint ( 0 , captcha_height ))
        draw . line ([ begin , end ], fill = self . get_line_color ())

    def  draw_point ( self , draw , point_chance , width , height ):
        '''
        Draw small dots
        :param draw: brush object
        :param point_chance: The probability of drawing a small dot is point_chance/100
        :param width: verification code width
        :param height: verification code height
        :return:
        '''
        # Randomly draw small dots according to probability
        for  w  in  range ( width ):
            for  h  in  range ( height ):
                tmp  =  Random . the randint ( 0 , 100 )
                if  tmp  <  point_chance :
                    draw . point (( w , h ), fill = self . get_line_color ())

    def  make_captcha ( self ):
        # Get the width and height of the verification code
        width , height  =  self . captcha_size
        # Generate a picture
        captcha  =  Image . new ( 'RGB' , self . captcha_size , self . background_color )
        # Get font object
        font  =  ImageFont . truetype ( 'simkai.ttf' , self . font_size )
        # Get the brush object
        draw  =  ImageDraw . Draw ( captcha )
        # Get the drawn characters
        text  =  self . get_text ()

        # Draw characters
        Self . draw_text ( Draw , text , font , width , height )

        # Draw lines
        for  i  in  range ( self . line_number ):
            Self . draw_line ( Draw , width , height )

        # Draw a small dot 10 is the probability 10/100, the probability of 10%
        Self . draw_point ( Draw , 10 , width , height )

        # save Picture
        captcha . save ( 'captcha' , format = self . format )
        # display image
        captcha . show ()

if  __name__  ==  ' __main__ ' :
    Captcha (). make_captcha ()