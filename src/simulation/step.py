from . import mobs, projectiles

# _mobs = mobs.Mobs()
# _projectiles = projectiles.Projectiles()
# _mobs.add(pos=(-1, 1), vel=(1, 0), acc=(0, 0.1))
# _mobs.add(pos=(1, 1), vel=(5, 1), acc=(-1, -1))
# _mobs.add(pos=(-1, -1), vel=(0, 0), acc=(3, 2))
# _mobs.add(pos=(1, -1), vel=(0, 0), acc=(1, 0.1))
# dt = 1
# count = 0
# while True:
#     count += 1
#     _mobs.update(dt)
#     _projectiles.update(dt)
#     # projectiles
#     if(random() > 0.3):
#         _projectiles.fire(pos=(random(), random()), dir=(random(), random()))
#
#     logger.info(f"[{count}] mobs: {_mobs._soa._end}, projectiles: {_projectiles._soa._end}")
#     if(count > 100):
#         break
