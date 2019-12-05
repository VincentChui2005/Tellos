from fly_tello import FlyTello
from playsound import playsound
from threading import Thread as thread
import time


fly = FlyTello(["0TQDG2KEDB4MCG",  # 1
                "0TQDG2KEDBT8F8",  # 2
                "0TQDG2KEDBU93L",  # 3
                "0TQDG2KEDBM40U",  # 4
                "0TQDG3KEDBY1J4"   # 5
                ])


def motion0():
    with fly.sync_these():
        fly.takeoff(tello=1)
        fly.takeoff(tello=2)
        fly.takeoff(tello=3)
        fly.takeoff(tello=4)
        fly.takeoff(tello=5)
    fly.reorient(50, pad='m-2')
    with fly.sync_these():
        fly.up(30, tello=1)
        fly.up(30, tello=2)
        fly.up(30, tello=3)
        fly.up(30, tello=4)
        fly.up(70, tello=5)


def motion1():
    with fly.sync_these():
        fly.straight_from_pad(x=-160, y=0, z=80, speed=100, pad='m1', tello=1)
        fly.straight_from_pad(x=0, y=160, z=80, speed=100, pad='m3', tello=2)
        fly.straight_from_pad(x=0, y=-160, z=80, speed=100, pad='m3', tello=3)
        fly.straight_from_pad(x=170, y=0, z=80, speed=100, pad='m1', tello=4)
        fly.straight_from_pad(x=0, y=0, z=180, speed=80, pad='m8', tello=5)

    time.sleep(3.5)
    with fly.sync_these():
        fly.curve_from_pad(x1=25, y1=-75, z1=100, x2=85, y2=-75, z2=120, speed=30, pad='m6', tello=1)
        fly.curve_from_pad(x1=-75, y1=-25, z1=100, x2=-75, y2=-75, z2=120, speed=30, pad='m2', tello=2)
        fly.curve_from_pad(x1=75, y1=25, z1=100, x2=75, y2=75, z2=120, speed=30, pad='m2', tello=3)
        fly.curve_from_pad(x1=-25, y1=75, z1=100, x2=-50, y2=75, z2=120, speed=30, pad='m6', tello=4)
    fly.reorient(height=80, pad='m8', tello=5)
    fly.reorient(height=120, pad='m-2')


def motion2():
    with fly.sync_these():
        fly.rotate_ccw(360, 1)
        fly.rotate_ccw(360, 2)
        fly.rotate_ccw(360, 3)
        fly.rotate_ccw(360, 4)
        fly.rotate_cw(360, 5)

    with fly.sync_these():
        fly.straight_from_pad(x=75, y=-75, z=80, speed=100, pad='m4', tello=1)
        time.sleep(2.5)
        fly.straight_from_pad(x=-75, y=-170, z=80, speed=100, pad='m5', tello=2)
        time.sleep(2.5)
        fly.straight_from_pad(x=75, y=170, z=80, speed=100, pad='m5', tello=3)
        time.sleep(2.5)
        fly.straight_from_pad(x=-75, y=75, z=80, speed=100, pad='m4', tello=4)


if __name__ == '__main__':
    # Thread naming
    # tellos
    intro_t = thread(target=motion0)
    verse1_t = thread(target=motion1)
    verse2_t = thread(target=motion2)
    # music
    intro_m = thread(target=playsound, args=("1 Intro.wav",))
    verse1_m = thread(target=playsound, args=("2 Verse.wav",))
    verse2_m = thread(target=playsound, args=("3 Verse 2.wav",))
    chorus_m = thread(target=playsound, args=("4 Chorus.wav",))
    pcomp_m = thread(target=playsound, args=("5 Pre-complex.wav",))
    comp_m = thread(target=playsound, args=("6 Complex.wav",))
    end_m = thread(target=playsound, args=("7 Ending.wav",))

    # Tello movement + Music
    intro_m.start()
    intro_t.start()
    intro_m.join()
    intro_t.join()

    verse1_m.start()
    verse1_t.start()
    verse1_m.join()
    verse1_t.join()

    verse2_m.start()
    verse2_t.start()
    verse2_m.join()
    verse2_t.join()


    # Ending just for now
    fly.land()
    time.sleep(1)






