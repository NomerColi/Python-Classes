import matplotlib.pyplot as plt
import numpy as np

b = True

if b:
    # grid for vector field
    x, y = np.meshgrid(np.arange(-5,5,1),np.arange(-5,5,1))
    # vector field (u,v)
    u = x/np.sqrt(x**2 + y**2)
    v = y/np.sqrt(x**2 + y**2)
    # plot vector field
    plt.quiver(x,y,u,v)

    # grid for contour
    x, y = np.meshgrid(np.arange(-5,5,0.1),np.arange(-5,5,0.1))

    #plot contour
    plt.contour(x,y,np.cos(3*x)+0.5*y**2,levels=10)

    plt.show()
else:
    # 3D vector field
    ax = plt.figure().add_subplot(projection='3d')

    # Make the grid
    x, y, z = np.meshgrid(np.arange(-2, 2, 0.5),
                        np.arange(-2, 2, 0.5),
                        np.arange(-2, 2, 0.5))

    # Make the direction data for the arrows
    u = 1
    v = 2
    w = z

    # plot the vector filed
    ax.quiver(x, y, z, u, v, w, length=0.3, normalize=True)

    plt.show()
