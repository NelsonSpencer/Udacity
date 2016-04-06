#!/usr/bin/env python
"""Call the instances of movie and store each movie's info"""
import fresh_tomatoes
import media



the_matrix = media.Movie(
						"The Matrix",
						"A dystopian future in which reality as perceived bymost humans is actually a simulated reality called 'the Matrix'.",
						"https://upload.wikimedia.org/wikipedia/en/c/c1/The_Matrix_Poster.jpg",# noqa
						"https://www.youtube.com/watch?v=m8e-FF8MsqU")# noqa



shawshank_redemption = media.Movie("Shawshank Redemption",
					 "The story of Andy Dufresne, a banker who is sentenced to life in Shawshank State Penitentiary for the murder of his wife and her lover, despite his claims of innocence..",
					 "https://upload.wikimedia.org/wikipedia/en/8/81/ShawshankRedemptionMoviePoster.jpg",# noqa
					 "https://www.youtube.com/watch?v=6hB3S9bIaco")# noqa


the_prestige = media.Movie("The Prestige",
						  "The story follows Robert Angier and Alfred Borden, rival stage magicians in London at the end of the 19th century. Obsessed with creating the best stage illusion, they engage in competitive one-upmanship with tragic results.",
						  "http://ecx.images-amazon.com/images/I/41I9XGrG88L.jpg",# noqa
						  "https://www.youtube.com/watch?v=o4gHCmTQDVI")# noqa

hunger_games = media.Movie("The Hunger Games",
						  "The Hunger Games universe is a dystopia set in 'Panem', a country consisting of the wealthy Capitol and twelve districts in varying states of poverty. Every year, children are chosen to participate in a compulsory annual televised death match called The Hunger Games.",
						  "https://upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg",# noqa
						  "https://www.youtube.com/watch?v=mfmrPu43DF8")# noqa

the_martian = media.Movie("The Martian",
						  "An astronaut who is mistakenly presumed dead and left behind on Mars. The film depicts his struggle to survive and others' efforts to rescue him.",
						  "https://upload.wikimedia.org/wikipedia/en/c/cd/The_Martian_film_poster.jpg",# noqa
						  "https://www.youtube.com/watch?v=ej3ioOneTy8")# noqa

concussion = media.Movie("Concussion",
						  "The film stars Will Smith as Dr. Bennet Omalu, a Nigerian forensic pathologist who fought against efforts by the National Football League to suppress his research on chronic traumatic encephalopathy (CTE) brain damage suffered by professional football players.",
						  "https://upload.wikimedia.org/wikipedia/en/e/ee/Concussion_poster.jpg",# noqa
						  "https://www.youtube.com/watch?v=Qk-1TLVUPZk")# noqa

#Add each movie to the list
movies = [the_matrix,shawshank_redemption,the_prestige,hunger_games,the_martian,concussion]
#Call open movies and display image
fresh_tomatoes.open_movies_page(movies)