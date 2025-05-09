#include <graphics.h>
#include <stdlib.h>
#include <stdio.h>
#include <conio.h>

void drawDashedLine(int x1, int y1, int x2, int y2) {
    int i;
    for (i = x1; i < x2; i += 10) {
        line(i, y1, i + 5, y1 + (y2 - y1) * (i + 5 - x1) / (x2 - x1));
    }
}

void drawDottedLine(int x1, int y1, int x2, int y2) {
    int i;
    for (i = x1; i < x2; i += 5) {
        putpixel(i, y1 + (y2 - y1) * (i - x1) / (x2 - x1), WHITE);
    }
}

void drawCenterLine(int x1, int y1, int x2, int y2) {
    int midX = (x1 + x2) / 2;
    line(midX, y1, midX, y2);
}

void drawSolidLine(int x1, int y1, int x2, int y2) {
    line(x1, y1, x2, y2);
}

int main() {
    int gd = DETECT, gm;
    initgraph(&gd, &gm, "C:\\Turboc3\\BGI");

    // Draw a simple horizontal line
    line(100, 100, 200, 100);

    // Draw a simple vertical line
    line(100, 100, 100, 200);

    // Draw a diagonal line
    line(100, 100, 200, 200);

    // Draw a dashed line
    drawDashedLine(100, 250, 300, 250);

    // Draw a dotted line
    drawDottedLine(100, 300, 300, 300);

    // Draw a center line
    drawCenterLine(100, 350, 300, 350);

    // Draw a solid line
    drawSolidLine(100, 400, 300, 400);

    getch();
    closegraph();
    return 0;
}