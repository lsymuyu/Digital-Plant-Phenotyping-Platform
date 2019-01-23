#declare grid  = L*cos(Ze/180*pi)*df/(pi+(2*cos(Ze/180*pi)-1)*pi*df)*(10/180*pi)*(10/180*pi);
#declare n_0   = grid*sin(0/180*pi);
#declare n_10  = grid*sin(10/180*pi);
#declare n_20  = grid*sin(20/180*pi);
#declare n_30  = grid*sin(30/180*pi);
#declare n_40  = grid*sin(40/180*pi);
#declare n_50  = grid*sin(50/180*pi);
#declare n_60  = grid*sin(60/180*pi);
#declare n_70  = grid*sin(70/180*pi);
#declare n_80  = grid*sin(80/180*pi);

// direct radiation 
light_source {<0,0,1000> color L*(1 - df)/(1+(2*cos(Ze/180*pi)-1)*df)*<1,1,1>  rotate <Ze, 0, Az> parallel}              // sun

// diffuse radiation
light_source {<0,0,1000> color n_0*<1,1,1>  rotate <0,0,0> parallel}

light_source {<0,0,1000> color n_10*<1,1,1>  rotate <10,0,0> parallel}
light_source {<0,0,1000> color n_20*<1,1,1>  rotate <20,0,0> parallel}
light_source {<0,0,1000> color n_30*<1,1,1>  rotate <30,0,0> parallel}
light_source {<0,0,1000> color n_40*<1,1,1>  rotate <40,0,0> parallel}
light_source {<0,0,1000> color n_50*<1,1,1>  rotate <50,0,0> parallel}
light_source {<0,0,1000> color n_60*<1,1,1>  rotate <60,0,0> parallel}
light_source {<0,0,1000> color n_70*<1,1,1>  rotate <70,0,0> parallel}
light_source {<0,0,1000> color n_80*<1,1,1>  rotate <80,0,0> parallel}

light_source {<0,0,1000> color n_10*<1,1,1>  rotate <10,0,10> parallel}
light_source {<0,0,1000> color n_20*<1,1,1>  rotate <20,0,10> parallel}
light_source {<0,0,1000> color n_30*<1,1,1>  rotate <30,0,10> parallel}
light_source {<0,0,1000> color n_40*<1,1,1>  rotate <40,0,10> parallel}
light_source {<0,0,1000> color n_50*<1,1,1>  rotate <50,0,10> parallel}
light_source {<0,0,1000> color n_60*<1,1,1>  rotate <60,0,10> parallel}
light_source {<0,0,1000> color n_70*<1,1,1>  rotate <70,0,10> parallel}
light_source {<0,0,1000> color n_80*<1,1,1>  rotate <80,0,10> parallel}

light_source {<0,0,1000> color n_10*<1,1,1>  rotate <10,0,20> parallel}
light_source {<0,0,1000> color n_20*<1,1,1>  rotate <20,0,20> parallel}
light_source {<0,0,1000> color n_30*<1,1,1>  rotate <30,0,20> parallel}
light_source {<0,0,1000> color n_40*<1,1,1>  rotate <40,0,20> parallel}
light_source {<0,0,1000> color n_50*<1,1,1>  rotate <50,0,20> parallel}
light_source {<0,0,1000> color n_60*<1,1,1>  rotate <60,0,20> parallel}
light_source {<0,0,1000> color n_70*<1,1,1>  rotate <70,0,20> parallel}
light_source {<0,0,1000> color n_80*<1,1,1>  rotate <80,0,20> parallel}

light_source {<0,0,1000> color n_10*<1,1,1>  rotate <10,0,30> parallel}
light_source {<0,0,1000> color n_20*<1,1,1>  rotate <20,0,30> parallel}
light_source {<0,0,1000> color n_30*<1,1,1>  rotate <30,0,30> parallel}
light_source {<0,0,1000> color n_40*<1,1,1>  rotate <40,0,30> parallel}
light_source {<0,0,1000> color n_50*<1,1,1>  rotate <50,0,30> parallel}
light_source {<0,0,1000> color n_60*<1,1,1>  rotate <60,0,30> parallel}
light_source {<0,0,1000> color n_70*<1,1,1>  rotate <70,0,30> parallel}
light_source {<0,0,1000> color n_80*<1,1,1>  rotate <80,0,30> parallel}

light_source {<0,0,1000> color n_10*<1,1,1>  rotate <10,0,40> parallel}
light_source {<0,0,1000> color n_20*<1,1,1>  rotate <20,0,40> parallel}
light_source {<0,0,1000> color n_30*<1,1,1>  rotate <30,0,40> parallel}
light_source {<0,0,1000> color n_40*<1,1,1>  rotate <40,0,40> parallel}
light_source {<0,0,1000> color n_50*<1,1,1>  rotate <50,0,40> parallel}
light_source {<0,0,1000> color n_60*<1,1,1>  rotate <60,0,40> parallel}
light_source {<0,0,1000> color n_70*<1,1,1>  rotate <70,0,40> parallel}
light_source {<0,0,1000> color n_80*<1,1,1>  rotate <80,0,40> parallel}   

light_source {<0,0,1000> color n_10*<1,1,1>  rotate <10,0,50> parallel}
light_source {<0,0,1000> color n_20*<1,1,1>  rotate <20,0,50> parallel}
light_source {<0,0,1000> color n_30*<1,1,1>  rotate <30,0,50> parallel}
light_source {<0,0,1000> color n_40*<1,1,1>  rotate <40,0,50> parallel}
light_source {<0,0,1000> color n_50*<1,1,1>  rotate <50,0,50> parallel}
light_source {<0,0,1000> color n_60*<1,1,1>  rotate <60,0,50> parallel}
light_source {<0,0,1000> color n_70*<1,1,1>  rotate <70,0,50> parallel}
light_source {<0,0,1000> color n_80*<1,1,1>  rotate <80,0,50> parallel}

light_source {<0,0,1000> color n_10*<1,1,1>  rotate <10,0,60> parallel}
light_source {<0,0,1000> color n_20*<1,1,1>  rotate <20,0,60> parallel}
light_source {<0,0,1000> color n_30*<1,1,1>  rotate <30,0,60> parallel}
light_source {<0,0,1000> color n_40*<1,1,1>  rotate <40,0,60> parallel}
light_source {<0,0,1000> color n_50*<1,1,1>  rotate <50,0,60> parallel}
light_source {<0,0,1000> color n_60*<1,1,1>  rotate <60,0,60> parallel}
light_source {<0,0,1000> color n_70*<1,1,1>  rotate <70,0,60> parallel}
light_source {<0,0,1000> color n_80*<1,1,1>  rotate <80,0,60> parallel}

light_source {<0,0,1000> color n_10*<1,1,1>  rotate <10,0,70> parallel}
light_source {<0,0,1000> color n_20*<1,1,1>  rotate <20,0,70> parallel}
light_source {<0,0,1000> color n_30*<1,1,1>  rotate <30,0,70> parallel}
light_source {<0,0,1000> color n_40*<1,1,1>  rotate <40,0,70> parallel}
light_source {<0,0,1000> color n_50*<1,1,1>  rotate <50,0,70> parallel}
light_source {<0,0,1000> color n_60*<1,1,1>  rotate <60,0,70> parallel}
light_source {<0,0,1000> color n_70*<1,1,1>  rotate <70,0,70> parallel}
light_source {<0,0,1000> color n_80*<1,1,1>  rotate <80,0,70> parallel}

light_source {<0,0,1000> color n_10*<1,1,1>  rotate <10,0,80> parallel}
light_source {<0,0,1000> color n_20*<1,1,1>  rotate <20,0,80> parallel}
light_source {<0,0,1000> color n_30*<1,1,1>  rotate <30,0,80> parallel}
light_source {<0,0,1000> color n_40*<1,1,1>  rotate <40,0,80> parallel}
light_source {<0,0,1000> color n_50*<1,1,1>  rotate <50,0,80> parallel}
light_source {<0,0,1000> color n_60*<1,1,1>  rotate <60,0,80> parallel}
light_source {<0,0,1000> color n_70*<1,1,1>  rotate <70,0,80> parallel}
light_source {<0,0,1000> color n_80*<1,1,1>  rotate <80,0,80> parallel}

light_source {<0,0,1000> color n_10*<1,1,1>  rotate <10,0,90> parallel}
light_source {<0,0,1000> color n_20*<1,1,1>  rotate <20,0,90> parallel}
light_source {<0,0,1000> color n_30*<1,1,1>  rotate <30,0,90> parallel}
light_source {<0,0,1000> color n_40*<1,1,1>  rotate <40,0,90> parallel}
light_source {<0,0,1000> color n_50*<1,1,1>  rotate <50,0,90> parallel}
light_source {<0,0,1000> color n_60*<1,1,1>  rotate <60,0,90> parallel}
light_source {<0,0,1000> color n_70*<1,1,1>  rotate <70,0,90> parallel}
light_source {<0,0,1000> color n_80*<1,1,1>  rotate <80,0,90> parallel}

light_source {<0,0,1000> color n_10*<1,1,1>  rotate <10,0,100> parallel}
light_source {<0,0,1000> color n_20*<1,1,1>  rotate <20,0,100> parallel}
light_source {<0,0,1000> color n_30*<1,1,1>  rotate <30,0,100> parallel}
light_source {<0,0,1000> color n_40*<1,1,1>  rotate <40,0,100> parallel}
light_source {<0,0,1000> color n_50*<1,1,1>  rotate <50,0,100> parallel}
light_source {<0,0,1000> color n_60*<1,1,1>  rotate <60,0,100> parallel}
light_source {<0,0,1000> color n_70*<1,1,1>  rotate <70,0,100> parallel}
light_source {<0,0,1000> color n_80*<1,1,1>  rotate <80,0,100> parallel}

light_source {<0,0,1000> color n_10*<1,1,1>  rotate <10,0,110> parallel}
light_source {<0,0,1000> color n_20*<1,1,1>  rotate <20,0,110> parallel}
light_source {<0,0,1000> color n_30*<1,1,1>  rotate <30,0,110> parallel}
light_source {<0,0,1000> color n_40*<1,1,1>  rotate <40,0,110> parallel}
light_source {<0,0,1000> color n_50*<1,1,1>  rotate <50,0,110> parallel}
light_source {<0,0,1000> color n_60*<1,1,1>  rotate <60,0,110> parallel}
light_source {<0,0,1000> color n_70*<1,1,1>  rotate <70,0,110> parallel}
light_source {<0,0,1000> color n_80*<1,1,1>  rotate <80,0,110> parallel}

light_source {<0,0,1000> color n_10*<1,1,1>  rotate <10,0,120> parallel}
light_source {<0,0,1000> color n_20*<1,1,1>  rotate <20,0,120> parallel}
light_source {<0,0,1000> color n_30*<1,1,1>  rotate <30,0,120> parallel}
light_source {<0,0,1000> color n_40*<1,1,1>  rotate <40,0,120> parallel}
light_source {<0,0,1000> color n_50*<1,1,1>  rotate <50,0,120> parallel}
light_source {<0,0,1000> color n_60*<1,1,1>  rotate <60,0,120> parallel}
light_source {<0,0,1000> color n_70*<1,1,1>  rotate <70,0,120> parallel}
light_source {<0,0,1000> color n_80*<1,1,1>  rotate <80,0,120> parallel}

light_source {<0,0,1000> color n_10*<1,1,1>  rotate <10,0,130> parallel}
light_source {<0,0,1000> color n_20*<1,1,1>  rotate <20,0,130> parallel}
light_source {<0,0,1000> color n_30*<1,1,1>  rotate <30,0,130> parallel}
light_source {<0,0,1000> color n_40*<1,1,1>  rotate <40,0,130> parallel}
light_source {<0,0,1000> color n_50*<1,1,1>  rotate <50,0,130> parallel}
light_source {<0,0,1000> color n_60*<1,1,1>  rotate <60,0,130> parallel}
light_source {<0,0,1000> color n_70*<1,1,1>  rotate <70,0,130> parallel}
light_source {<0,0,1000> color n_80*<1,1,1>  rotate <80,0,130> parallel}

light_source {<0,0,1000> color n_10*<1,1,1>  rotate <10,0,140> parallel}
light_source {<0,0,1000> color n_20*<1,1,1>  rotate <20,0,140> parallel}
light_source {<0,0,1000> color n_30*<1,1,1>  rotate <30,0,140> parallel}
light_source {<0,0,1000> color n_40*<1,1,1>  rotate <40,0,140> parallel}
light_source {<0,0,1000> color n_50*<1,1,1>  rotate <50,0,140> parallel}
light_source {<0,0,1000> color n_60*<1,1,1>  rotate <60,0,140> parallel}
light_source {<0,0,1000> color n_70*<1,1,1>  rotate <70,0,140> parallel}
light_source {<0,0,1000> color n_80*<1,1,1>  rotate <80,0,140> parallel}

light_source {<0,0,1000> color n_10*<1,1,1>  rotate <10,0,150> parallel}
light_source {<0,0,1000> color n_20*<1,1,1>  rotate <20,0,150> parallel}
light_source {<0,0,1000> color n_30*<1,1,1>  rotate <30,0,150> parallel}
light_source {<0,0,1000> color n_40*<1,1,1>  rotate <40,0,150> parallel}
light_source {<0,0,1000> color n_50*<1,1,1>  rotate <50,0,150> parallel}
light_source {<0,0,1000> color n_60*<1,1,1>  rotate <60,0,150> parallel}
light_source {<0,0,1000> color n_70*<1,1,1>  rotate <70,0,150> parallel}
light_source {<0,0,1000> color n_80*<1,1,1>  rotate <80,0,150> parallel}

light_source {<0,0,1000> color n_10*<1,1,1>  rotate <10,0,160> parallel}
light_source {<0,0,1000> color n_20*<1,1,1>  rotate <20,0,160> parallel}
light_source {<0,0,1000> color n_30*<1,1,1>  rotate <30,0,160> parallel}
light_source {<0,0,1000> color n_40*<1,1,1>  rotate <40,0,160> parallel}
light_source {<0,0,1000> color n_50*<1,1,1>  rotate <50,0,160> parallel}
light_source {<0,0,1000> color n_60*<1,1,1>  rotate <60,0,160> parallel}
light_source {<0,0,1000> color n_70*<1,1,1>  rotate <70,0,160> parallel}
light_source {<0,0,1000> color n_80*<1,1,1>  rotate <80,0,160> parallel}   

light_source {<0,0,1000> color n_10*<1,1,1>  rotate <10,0,170> parallel}
light_source {<0,0,1000> color n_20*<1,1,1>  rotate <20,0,170> parallel}
light_source {<0,0,1000> color n_30*<1,1,1>  rotate <30,0,170> parallel}
light_source {<0,0,1000> color n_40*<1,1,1>  rotate <40,0,170> parallel}
light_source {<0,0,1000> color n_50*<1,1,1>  rotate <50,0,170> parallel}
light_source {<0,0,1000> color n_60*<1,1,1>  rotate <60,0,170> parallel}
light_source {<0,0,1000> color n_70*<1,1,1>  rotate <70,0,170> parallel}
light_source {<0,0,1000> color n_80*<1,1,1>  rotate <80,0,170> parallel}

light_source {<0,0,1000> color n_10*<1,1,1>  rotate <10,0,180> parallel}
light_source {<0,0,1000> color n_20*<1,1,1>  rotate <20,0,180> parallel}
light_source {<0,0,1000> color n_30*<1,1,1>  rotate <30,0,180> parallel}
light_source {<0,0,1000> color n_40*<1,1,1>  rotate <40,0,180> parallel}
light_source {<0,0,1000> color n_50*<1,1,1>  rotate <50,0,180> parallel}
light_source {<0,0,1000> color n_60*<1,1,1>  rotate <60,0,180> parallel}
light_source {<0,0,1000> color n_70*<1,1,1>  rotate <70,0,180> parallel}
light_source {<0,0,1000> color n_80*<1,1,1>  rotate <80,0,180> parallel}

light_source {<0,0,1000> color n_10*<1,1,1>  rotate <10,0,190> parallel}
light_source {<0,0,1000> color n_20*<1,1,1>  rotate <20,0,190> parallel}
light_source {<0,0,1000> color n_30*<1,1,1>  rotate <30,0,190> parallel}
light_source {<0,0,1000> color n_40*<1,1,1>  rotate <40,0,190> parallel}
light_source {<0,0,1000> color n_50*<1,1,1>  rotate <50,0,190> parallel}
light_source {<0,0,1000> color n_60*<1,1,1>  rotate <60,0,190> parallel}
light_source {<0,0,1000> color n_70*<1,1,1>  rotate <70,0,190> parallel}
light_source {<0,0,1000> color n_80*<1,1,1>  rotate <80,0,190> parallel}

light_source {<0,0,1000> color n_10*<1,1,1>  rotate <10,0,200> parallel}
light_source {<0,0,1000> color n_20*<1,1,1>  rotate <20,0,200> parallel}
light_source {<0,0,1000> color n_30*<1,1,1>  rotate <30,0,200> parallel}
light_source {<0,0,1000> color n_40*<1,1,1>  rotate <40,0,200> parallel}
light_source {<0,0,1000> color n_50*<1,1,1>  rotate <50,0,200> parallel}
light_source {<0,0,1000> color n_60*<1,1,1>  rotate <60,0,200> parallel}
light_source {<0,0,1000> color n_70*<1,1,1>  rotate <70,0,200> parallel}
light_source {<0,0,1000> color n_80*<1,1,1>  rotate <80,0,200> parallel}

light_source {<0,0,1000> color n_10*<1,1,1>  rotate <10,0,210> parallel}
light_source {<0,0,1000> color n_20*<1,1,1>  rotate <20,0,210> parallel}
light_source {<0,0,1000> color n_30*<1,1,1>  rotate <30,0,210> parallel}
light_source {<0,0,1000> color n_40*<1,1,1>  rotate <40,0,210> parallel}
light_source {<0,0,1000> color n_50*<1,1,1>  rotate <50,0,210> parallel}
light_source {<0,0,1000> color n_60*<1,1,1>  rotate <60,0,210> parallel}
light_source {<0,0,1000> color n_70*<1,1,1>  rotate <70,0,210> parallel}
light_source {<0,0,1000> color n_80*<1,1,1>  rotate <80,0,210> parallel}

light_source {<0,0,1000> color n_10*<1,1,1>  rotate <10,0,220> parallel}
light_source {<0,0,1000> color n_20*<1,1,1>  rotate <20,0,220> parallel}
light_source {<0,0,1000> color n_30*<1,1,1>  rotate <30,0,220> parallel}
light_source {<0,0,1000> color n_40*<1,1,1>  rotate <40,0,220> parallel}
light_source {<0,0,1000> color n_50*<1,1,1>  rotate <50,0,220> parallel}
light_source {<0,0,1000> color n_60*<1,1,1>  rotate <60,0,220> parallel}
light_source {<0,0,1000> color n_70*<1,1,1>  rotate <70,0,220> parallel}
light_source {<0,0,1000> color n_80*<1,1,1>  rotate <80,0,220> parallel}

light_source {<0,0,1000> color n_10*<1,1,1>  rotate <10,0,230> parallel}
light_source {<0,0,1000> color n_20*<1,1,1>  rotate <20,0,230> parallel}
light_source {<0,0,1000> color n_30*<1,1,1>  rotate <30,0,230> parallel}
light_source {<0,0,1000> color n_40*<1,1,1>  rotate <40,0,230> parallel}
light_source {<0,0,1000> color n_50*<1,1,1>  rotate <50,0,230> parallel}
light_source {<0,0,1000> color n_60*<1,1,1>  rotate <60,0,230> parallel}
light_source {<0,0,1000> color n_70*<1,1,1>  rotate <70,0,230> parallel}
light_source {<0,0,1000> color n_80*<1,1,1>  rotate <80,0,230> parallel}

light_source {<0,0,1000> color n_10*<1,1,1>  rotate <10,0,240> parallel}
light_source {<0,0,1000> color n_20*<1,1,1>  rotate <20,0,240> parallel}
light_source {<0,0,1000> color n_30*<1,1,1>  rotate <30,0,240> parallel}
light_source {<0,0,1000> color n_40*<1,1,1>  rotate <40,0,240> parallel}
light_source {<0,0,1000> color n_50*<1,1,1>  rotate <50,0,240> parallel}
light_source {<0,0,1000> color n_60*<1,1,1>  rotate <60,0,240> parallel}
light_source {<0,0,1000> color n_70*<1,1,1>  rotate <70,0,240> parallel}
light_source {<0,0,1000> color n_80*<1,1,1>  rotate <80,0,240> parallel}

light_source {<0,0,1000> color n_10*<1,1,1>  rotate <10,0,250> parallel}
light_source {<0,0,1000> color n_20*<1,1,1>  rotate <20,0,250> parallel}
light_source {<0,0,1000> color n_30*<1,1,1>  rotate <30,0,250> parallel}
light_source {<0,0,1000> color n_40*<1,1,1>  rotate <40,0,250> parallel}
light_source {<0,0,1000> color n_50*<1,1,1>  rotate <50,0,250> parallel}
light_source {<0,0,1000> color n_60*<1,1,1>  rotate <60,0,250> parallel}
light_source {<0,0,1000> color n_70*<1,1,1>  rotate <70,0,250> parallel}
light_source {<0,0,1000> color n_80*<1,1,1>  rotate <80,0,250> parallel}

light_source {<0,0,1000> color n_10*<1,1,1>  rotate <10,0,260> parallel}
light_source {<0,0,1000> color n_20*<1,1,1>  rotate <20,0,260> parallel}
light_source {<0,0,1000> color n_30*<1,1,1>  rotate <30,0,260> parallel}
light_source {<0,0,1000> color n_40*<1,1,1>  rotate <40,0,260> parallel}
light_source {<0,0,1000> color n_50*<1,1,1>  rotate <50,0,260> parallel}
light_source {<0,0,1000> color n_60*<1,1,1>  rotate <60,0,260> parallel}
light_source {<0,0,1000> color n_70*<1,1,1>  rotate <70,0,260> parallel}
light_source {<0,0,1000> color n_80*<1,1,1>  rotate <80,0,260> parallel}   

light_source {<0,0,1000> color n_10*<1,1,1>  rotate <10,0,270> parallel}
light_source {<0,0,1000> color n_20*<1,1,1>  rotate <20,0,270> parallel}
light_source {<0,0,1000> color n_30*<1,1,1>  rotate <30,0,270> parallel}
light_source {<0,0,1000> color n_40*<1,1,1>  rotate <40,0,270> parallel}
light_source {<0,0,1000> color n_50*<1,1,1>  rotate <50,0,270> parallel}
light_source {<0,0,1000> color n_60*<1,1,1>  rotate <60,0,270> parallel}
light_source {<0,0,1000> color n_70*<1,1,1>  rotate <70,0,270> parallel}
light_source {<0,0,1000> color n_80*<1,1,1>  rotate <80,0,270> parallel}

light_source {<0,0,1000> color n_10*<1,1,1>  rotate <10,0,280> parallel}
light_source {<0,0,1000> color n_20*<1,1,1>  rotate <20,0,280> parallel}
light_source {<0,0,1000> color n_30*<1,1,1>  rotate <30,0,280> parallel}
light_source {<0,0,1000> color n_40*<1,1,1>  rotate <40,0,280> parallel}
light_source {<0,0,1000> color n_50*<1,1,1>  rotate <50,0,280> parallel}
light_source {<0,0,1000> color n_60*<1,1,1>  rotate <60,0,280> parallel}
light_source {<0,0,1000> color n_70*<1,1,1>  rotate <70,0,280> parallel}
light_source {<0,0,1000> color n_80*<1,1,1>  rotate <80,0,280> parallel}

light_source {<0,0,1000> color n_10*<1,1,1>  rotate <10,0,290> parallel}
light_source {<0,0,1000> color n_20*<1,1,1>  rotate <20,0,290> parallel}
light_source {<0,0,1000> color n_30*<1,1,1>  rotate <30,0,290> parallel}
light_source {<0,0,1000> color n_40*<1,1,1>  rotate <40,0,290> parallel}
light_source {<0,0,1000> color n_50*<1,1,1>  rotate <50,0,290> parallel}
light_source {<0,0,1000> color n_60*<1,1,1>  rotate <60,0,290> parallel}
light_source {<0,0,1000> color n_70*<1,1,1>  rotate <70,0,290> parallel}
light_source {<0,0,1000> color n_80*<1,1,1>  rotate <80,0,290> parallel}

light_source {<0,0,1000> color n_10*<1,1,1>  rotate <10,0,300> parallel}
light_source {<0,0,1000> color n_20*<1,1,1>  rotate <20,0,300> parallel}
light_source {<0,0,1000> color n_30*<1,1,1>  rotate <30,0,300> parallel}
light_source {<0,0,1000> color n_40*<1,1,1>  rotate <40,0,300> parallel}
light_source {<0,0,1000> color n_50*<1,1,1>  rotate <50,0,300> parallel}
light_source {<0,0,1000> color n_60*<1,1,1>  rotate <60,0,300> parallel}
light_source {<0,0,1000> color n_70*<1,1,1>  rotate <70,0,300> parallel}
light_source {<0,0,1000> color n_80*<1,1,1>  rotate <80,0,300> parallel}

light_source {<0,0,1000> color n_10*<1,1,1>  rotate <10,0,310> parallel}
light_source {<0,0,1000> color n_20*<1,1,1>  rotate <20,0,310> parallel}
light_source {<0,0,1000> color n_30*<1,1,1>  rotate <30,0,310> parallel}
light_source {<0,0,1000> color n_40*<1,1,1>  rotate <40,0,310> parallel}
light_source {<0,0,1000> color n_50*<1,1,1>  rotate <50,0,310> parallel}
light_source {<0,0,1000> color n_60*<1,1,1>  rotate <60,0,310> parallel}
light_source {<0,0,1000> color n_70*<1,1,1>  rotate <70,0,310> parallel}
light_source {<0,0,1000> color n_80*<1,1,1>  rotate <80,0,310> parallel}

light_source {<0,0,1000> color n_10*<1,1,1>  rotate <10,0,320> parallel}
light_source {<0,0,1000> color n_20*<1,1,1>  rotate <20,0,320> parallel}
light_source {<0,0,1000> color n_30*<1,1,1>  rotate <30,0,320> parallel}
light_source {<0,0,1000> color n_40*<1,1,1>  rotate <40,0,320> parallel}
light_source {<0,0,1000> color n_50*<1,1,1>  rotate <50,0,320> parallel}
light_source {<0,0,1000> color n_60*<1,1,1>  rotate <60,0,320> parallel}
light_source {<0,0,1000> color n_70*<1,1,1>  rotate <70,0,320> parallel}
light_source {<0,0,1000> color n_80*<1,1,1>  rotate <80,0,320> parallel}

light_source {<0,0,1000> color n_10*<1,1,1>  rotate <10,0,330> parallel}
light_source {<0,0,1000> color n_20*<1,1,1>  rotate <20,0,330> parallel}
light_source {<0,0,1000> color n_30*<1,1,1>  rotate <30,0,330> parallel}
light_source {<0,0,1000> color n_40*<1,1,1>  rotate <40,0,330> parallel}
light_source {<0,0,1000> color n_50*<1,1,1>  rotate <50,0,330> parallel}
light_source {<0,0,1000> color n_60*<1,1,1>  rotate <60,0,330> parallel}
light_source {<0,0,1000> color n_70*<1,1,1>  rotate <70,0,330> parallel}
light_source {<0,0,1000> color n_80*<1,1,1>  rotate <80,0,330> parallel}

light_source {<0,0,1000> color n_10*<1,1,1>  rotate <10,0,340> parallel}
light_source {<0,0,1000> color n_20*<1,1,1>  rotate <20,0,340> parallel}
light_source {<0,0,1000> color n_30*<1,1,1>  rotate <30,0,340> parallel}
light_source {<0,0,1000> color n_40*<1,1,1>  rotate <40,0,340> parallel}
light_source {<0,0,1000> color n_50*<1,1,1>  rotate <50,0,340> parallel}
light_source {<0,0,1000> color n_60*<1,1,1>  rotate <60,0,340> parallel}
light_source {<0,0,1000> color n_70*<1,1,1>  rotate <70,0,340> parallel}
light_source {<0,0,1000> color n_80*<1,1,1>  rotate <80,0,340> parallel}

light_source {<0,0,1000> color n_10*<1,1,1>  rotate <10,0,350> parallel}
light_source {<0,0,1000> color n_20*<1,1,1>  rotate <20,0,350> parallel}
light_source {<0,0,1000> color n_30*<1,1,1>  rotate <30,0,350> parallel}
light_source {<0,0,1000> color n_40*<1,1,1>  rotate <40,0,350> parallel}
light_source {<0,0,1000> color n_50*<1,1,1>  rotate <50,0,350> parallel}
light_source {<0,0,1000> color n_60*<1,1,1>  rotate <60,0,350> parallel}
light_source {<0,0,1000> color n_70*<1,1,1>  rotate <70,0,350> parallel}
light_source {<0,0,1000> color n_80*<1,1,1>  rotate <80,0,350> parallel}