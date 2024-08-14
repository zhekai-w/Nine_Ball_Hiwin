import tableball as table

cuex, cuey, ballx_set, bally_set, ballcount = table.generate_balls(8, table.radius)
table.main(ballx_set, bally_set, ballcount, cuex, cuey)
