import pygame

# initialize pygame mixer
pygame.mixer.init()

# set up the screen
pygame.init()
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Music Player")

# load the music files
music_files = ["Bohemian Rhapsody.mp3", "Don't Stop Me Now.mp3",
               "Killer Queen.mp3", "Another One Bites The Dust.mp3"]
current_music = 0
pygame.mixer.music.load(music_files[current_music])

# set up the font
font = pygame.font.SysFont(None, 48)

# define the text labels
play_text = font.render("Play", True, (0, 128, 0))
stop_text = font.render("Stop", True, (128, 0, 0))
next_text = font.render("Next", True, (0, 0, 128))
prev_text = font.render("Prev", True, (128, 128, 0))

# set up the positions of the text labels
play_rect = play_text.get_rect()
play_rect.center = (50, 125)
stop_rect = stop_text.get_rect()
stop_rect.center = (150, 125)
next_rect = next_text.get_rect()
next_rect.center = (250, 125)
prev_rect = prev_text.get_rect()
prev_rect.center = (350, 125)

# start the music
pygame.mixer.music.play()

# main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.stop()
                else:
                    pygame.mixer.music.play()
            elif event.key == pygame.K_RIGHT:
                current_music = (current_music + 1) % len(music_files)
                pygame.mixer.music.load(music_files[current_music])
                pygame.mixer.music.play()
            elif event.key == pygame.K_LEFT:
                current_music = (current_music - 1) % len(music_files)
                pygame.mixer.music.load(music_files[current_music])
                pygame.mixer.music.play()

    # draw the text labels
    screen.fill((255, 255, 255))
    screen.blit(play_text, play_rect)
    screen.blit(stop_text, stop_rect)
    screen.blit(next_text, next_rect)
    screen.blit(prev_text, prev_rect)
    pygame.display.flip()

# quit pygame
pygame.quit()
