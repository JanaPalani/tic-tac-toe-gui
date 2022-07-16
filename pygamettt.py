#  importing the packges needed 
import pygame
import time
# initialise pygame 
pygame.init()

# set the window size 
display=pygame.display.set_mode((600,600))


# settign the caption for the game 
pygame.display.set_caption("xo in pygame")

mouse = []

counter = 0
n=0
number={}
for i in range(1,10):
    number[i]=0

# setting the box values in the dictionary 
assignnumber={
    1:(0,0),2:(1,0),3:(2,0),4:(0,1),5:(1,1),6:(2,1),7:(0,2),8:(1,2),9:(2,2)
}
keys = [key for key,value in assignnumber.items()]
value = [value for key,value in assignnumber.items()]


# the condiotn to check for teh win 
condition = [(1,2,3),(4,5,6),(7,8,9),(1,4,7),(2,5,8),(3,6,9),(1,5,9),(3,5,7)]

#  this fuction is to draw 'x' for te click 
def x_val(k):
    for i in range(3):
        for j in range(3):
                if 0+(j*200) < k[0] and k[0] < 200+(j*200) and 0+(i*200) < k[1] and k[1] < 200+(i*200):
                    pygame.draw.line(display,(0,225,0),(25+(j*200),25+(i*200)),(175+(j*200),175+(i*200)),4)
                    pygame.draw.line(display,(0,225,0),(175+(j*200),25+(i*200)),(25+(j*200),175+(i*200)),4)
                    for n in value:
                        if  (j,i) == n:
                            num=keys[value.index(n)]
                            number[num]='x'

# this fuction is to draw 'o' for the click 
def o_val(k):
    for i in range(3):
        for j in range(3):
            if 0+(j*200) < k[0] and k[0] < 200+(j*200) and 0+(i*200) < k[1] and k[1] < 200+(i*200):
                pygame.draw.circle(display,(0,0,225),(100+(j*200),100+(i*200)),75,3)
                for k in value:
                    if (j,i) == k:
                        num=keys[value.index(k)]
                        number[num]='o'


def main():
    run=True

    while run:
        # fill the window with the background 
        display.fill((0,0,0))
        # clock.tick(1)


        #drawing the lines int he board of the display to play the tictac toe
        line1r=pygame.draw.line(display,(225,0,0),(0,200),(600,200),1)
        line2r=pygame.draw.line(display,(225,0,0),(0,400),(600,400),1)
        line1c=pygame.draw.line(display,(225,0,0),(200,0),(200,600),1)
        line2c=pygame.draw.line(display,(225,0,0),(400,0),(400,600),1)
        
        
        
        for event in pygame.event.get():
            #  to quit the window or to stop the game
            if event.type==pygame.QUIT:
                run = False

            # to get the position of the mouse click 
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos=pygame.mouse.get_pos()  
                mousex=pos[0]
                mousey=pos[1]
                mouse_click = [mousex,mousey]
                for i in range(3):
                    for j in range(3):
                        #  check on which box the mouse is clicked on
                        if 0+(j*200) < mouse_click[0] and mouse_click[0] < 200+(j*200) and 0+(i*200) < mouse_click[1] and mouse_click[1] < 200+(i*200):
                            for k in value:
                                if (j,i)==k:
                                    num=keys[value.index(k)]
                                    if number[num]==0:
                                        # appending each click of the mouse in a list 
                                        mouse.append(mouse_click)


        # giving the first click to x player and second click to o player 
        for index, pos in enumerate(mouse):
            if index % 2 == 0:    
                    x_val(pos)

            else:
                o_val(pos)

        # check whether all teh boxes are filled 
        values_num = [value for key,value in number.items() ]
        if 0 not in values_num:
            run = False
        
        # checkimg the winning condition of the players 
        for check in condition :
            if number[check[0]] == number[check[1]] == number[check[2]] !=0 :

                run = False
            # condition for the 'x' player to win 
            if number[check[0]] == number[check[1]] == number[check[2]] =='x' :

                print(f"x is winner")
                run = False
            # condition for the 'o' player to win
            if number[check[0]] == number[check[1]] == number[check[2]] =='o' :
                print(f'o is winner')
                run = False      
                
        # updating the window for each loop
        pygame.display.flip()

if __name__ == "__main__":
    main()
