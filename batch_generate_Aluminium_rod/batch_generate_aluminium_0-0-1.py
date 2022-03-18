# -*- coding: UTF-8 -*-
# Write Python 2 code in this online editor and run it.
cengshu=6
current_cs=1
radius=0.005
mk_value=1
x,y,z=0.0,0.0,0.0
def print_to_screen(mk,radius,x1,y1,z1,x2,y2,z2):
	txt='''					<setmkbound mk="{0}"/>
					<drawcylinder radius="{1:.3f}" >
						<point x="{2:.4f}" y="{3:.4f}" z="{4:.4f}" />
						<point x="{5:.4f}" y="{6:.4f}" z="{7:.4f}" />
					</drawcylinder>
'''
	print(txt.format(mk,radius,x1,y1,z1,x2,y2,z2))
def print_to_file(file,mk,radius,x1,y1,z1,x2,y2,z2):
	txt='''					<setmkbound mk="{0}"/>
					<drawcylinder radius="{1:.3f}" >
						<point x="{2:.4f}" y="{3:.4f}" z="{4:.4f}" />
						<point x="{5:.4f}" y="{6:.4f}" z="{7:.4f}" />
					</drawcylinder>
'''
	file.write(txt.format(mk,radius,x1,y1,z1,x2,y2,z2))
def generatecylinder(mk,radius,x1,y1,z1,x2,y2,z2):
	print_to_screen(mk,radius,x1,y1,z1,x2,y2,z2)
	file = open("demofile3.txt", "a")
	print_to_file(file,mk,radius,x1,y1,z1,x2,y2,z2)
	file.close()
def main(cs,ra,mk,origin_x,origin_y,origin_z,c_cs,odd_num_parti=6,double_num_parti=5):
        center_z=origin_z+0.005
        while c_cs<=cs:
                if(c_cs%2)==1:
                        center_x=origin_x+0.005
                        center_y=origin_y+0.0
                        odd_count=0
                        while odd_count<odd_num_parti:
                                generatecylinder(mk,ra,center_x,center_y,center_z,center_x,-center_y,center_z)
                                mk+=1
                                center_x=center_x+0.01
                                odd_count+=1
                else:
                        center_x=origin_x+0.01
                        center_y=origin_y+0.0
                        double_count=0
                        while double_count<double_num_parti:
                                generatecylinder(mk,ra,center_x,center_y,center_z,center_x,-center_y,center_z)
                                mk+=1
                                center_x=center_x+0.01
                                double_count+=1
                c_cs+=1
                center_z=center_z+0.005*pow(3,0.5)
main(cengshu,radius,mk_value,x,y,z,current_cs)
