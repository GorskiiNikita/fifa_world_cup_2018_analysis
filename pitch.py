# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 15:32:47 2019

@author: sgolovan
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

def plotPitch(annotations=False):
    plt.gcf().gca().add_artist(plt.Rectangle((-3,-2), 126, 84,
                                             linewidth=0,
                                             facecolor='g',
                                             zorder=-2))
    # Outer boundaries
    plt.plot([0,120,120,0,0], [0,0,80,80,0], color='w', zorder=-1)
    # The half-way line
    plt.plot([60,60], [0,80], color='w', zorder=-1)
    # Goals
    plt.plot([0,-2,-2,0], [36,36,44,44], color='w', zorder=-1)
    plt.plot([120,122,122,120], [36,36,44,44], color='w', zorder=-1)
    # Goal area
    plt.plot([0,6,6,0], [30,30,50,50], color='w', zorder=-1)
    plt.plot([120,114,114,120], [30,30,50,50], color='w', zorder=-1)
    # Penalty area
    plt.plot([0,18,18,0], [18,18,62,62], color='w', zorder=-1)
    plt.plot([120,102,102,120], [18,18,62,62], color='w', zorder=-1)
    # Penalty and the center spots
    plt.scatter([12,60,108], [40,40,40], s=10, color='w', zorder=-1)
    # Center circle
    plt.gcf().gca().add_artist(plt.Circle((60,40), 10, fill=False,
                                          linewidth=1.5, color='w', zorder=-1))
    # Penalty arcs
    plt.gcf().gca().add_artist(mpatches.Arc((12,40), 20, 20, 180, 126.87, 233.13,
                                            linewidth=1.5, color='w', zorder=-1))
    plt.gcf().gca().add_artist(mpatches.Arc((108,40), 20, 20, 0, 126.87, 233.13,
                                            linewidth=1.5, color='w', zorder=-1))
    # Corner arcs
    plt.gcf().gca().add_artist(mpatches.Arc((0,0), 2, 2, 0, 0, 90,
                                            linewidth=1.5, color='w', zorder=-1))
    plt.gcf().gca().add_artist(mpatches.Arc((120,0), 2, 2, 90, 0, 90,
                                            linewidth=1.5, color='w', zorder=-1))
    plt.gcf().gca().add_artist(mpatches.Arc((120,80), 2, 2, 180, 0, 90,
                                            linewidth=1.5, color='w', zorder=-1))
    plt.gcf().gca().add_artist(mpatches.Arc((0,80), 2, 2, -90, 0, 90,
                                            linewidth=1.5, color='w', zorder=-1))
    # Invert the Y-axis (to point downwards)
    plt.gca().invert_yaxis()
    # Remove the figure border and ticks
    plt.gcf().gca().set_frame_on(False)
    plt.gcf().gca().axes.get_xaxis().set_visible(False)
    plt.gcf().gca().axes.get_yaxis().set_visible(False)
    
    if annotations:
        # Add some annotations
        plt.annotate("0,0", (2,2), ha='left', va='top')
        plt.annotate("120,0", (118,2), ha='right', va='top')
        plt.annotate("0,80", (2,78), ha='left', va='bottom')
        plt.annotate("120,80", (118,78), ha='right', va='bottom')
        plt.annotate("18,62", (19,63), ha='left', va='top')
        plt.annotate("102,62", (101,63), ha='right', va='top')
        plt.annotate("18,18", (19,17), ha='left', va='bottom')
        plt.annotate("102,18", (101,17), ha='right', va='bottom')

