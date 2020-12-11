#include <SDL2/SDL.h>

#define XSIZE 600
#define YSIZE 600
#define MS 10

typedef struct Nave Nave;
typedef struct Misil Misil;
struct Nave
{
	int x1, y1;
	int x2, y2;
	int x3, y3;
	int vx, vy;
	Misil *misiles;
};

struct Misil
{
	int x1, y1;
	int x2, y2;
	int vx, vy;
};

void navePinta(Nave *nave, SDL_Renderer *renderer);

int main(void)
{
	if(SDL_Init(SDL_INIT_EVERYTHING) < 0)
	{
		SDL_ShowSimpleMessageBox(SDL_MESSAGEBOX_ERROR, "Error", SDL_GetError(),NULL);
		SDL_Quit();
		return (-1);
	}
	else
	{
		SDL_ShowSimpleMessageBox(SDL_MESSAGEBOX_INFORMATION, "OK", "SDL INIT", NULL);		
	}
	const unsigned char *keys;
	int gameOver = 0, typeEvent;
	SDL_Window *window;
	SDL_Renderer *renderer;
	SDL_Event event;
	Nave nave =  { XSIZE/2, YSIZE/2, XSIZE/2 -20, YSIZE/2 + 20, XSIZE/2 + 20, YSIZE/2 +20, 5, 5, NULL};
	window = SDL_CreateWindow("Juego Nave",SDL_WINDOWPOS_UNDEFINED,SDL_WINDOWPOS_UNDEFINED, XSIZE, YSIZE, SDL_WINDOW_SHOWN);
	renderer = SDL_CreateRenderer(window, -1, SDL_RENDERER_ACCELERATED);
	keys = SDL_GetKeyboardState(NULL);
	
	while(!gameOver)
	{
		if (SDL_PollEvent(&event))
		{
			// Handle events
			typeEvent = event.type;
			if (typeEvent == SDL_QUIT)
			{
				gameOver = 1;
			} 
			else if (typeEvent == SDL_MOUSEBUTTONDOWN)
			{
				if (SDL_GetMouseState(NULL,NULL) &
				SDL_BUTTON(SDL_BUTTON_LEFT))
				{
					//pendiente
				}
			}
			else if (typeEvent == SDL_KEYDOWN)
			{
				if (keys[SDL_SCANCODE_ESCAPE])
				{
					gameOver = 1;
				} 
				else if (keys[SDL_SCANCODE_LEFT])
				{

				}
				else if(keys[SDL_SCANCODE_RIGHT])
				{

				}
				else if(keys[SDL_SCANCODE_UP])
				{

				}
				else if(keys[SDL_SCANCODE_DOWN])
				{

				}
				else if(keys[SDL_SCANCODE_SPACE])
				{

				}
			}

			//pantalla
			SDL_SetRenderDrawColor(renderer,0, 0, 0, 0);
			SDL_RenderClear(renderer);
			SDL_SetRenderDrawColor(renderer, 255, 255, 255, 0);
			navePinta(&nave, renderer);
			SDL_RenderPresent(renderer);
			SDL_Delay(MS);
		}
	}
	SDL_DestroyRenderer(renderer);
	SDL_DestroyWindow(window);
	SDL_Quit();
	return (0);
}

void navePinta(Nave *nave, SDL_Renderer *renderer)
{
	
	SDL_Point points[4] =
	{
		{nave->x1, nave->y1},
		{nave->x2, nave->y2},
		{nave->x3, nave->y3}
	};
	points[3] = points[0];
	SDL_RenderDrawLines(renderer, points,4);
}
