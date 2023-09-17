import sys
import os
import glob
import hdf5_getters
import re
import tables

class Movie:
    MovieCount = 0
    # MovieDictionary = {}

    def __init__(self, MovieID):
        self.id = MovieID
        Movie.MovieCount += 1
        # Movie.MovieDictionary[MovieID] = self

        self.stars = None
        self.certificate = None
        self.duration = None
        self.genre = []
        self.description = None
        self.rating = None
        self.title = None
        self.year = None

    def displayMovieCount(self):
        print("Total Movie Count %i" % Movie.MovieCount)

    def displayMovie(self):
        print("ID: %s" % self.id )


def main():
    outputFile1 = open('n_movies.csv', 'w')
    csvRowString = ""

    print(outputFile1)

    #################################################
    #if you want to prompt the user for the order of attributes in the csv,
    #leave the prompt boolean set to True
    #else, set 'prompt' to False and set the order of attributes in the 'else'
    #clause
    prompt = False
    #################################################
    if prompt == True:
        while prompt:

            prompt = False

            csvAttributeString = raw_input("\n\nIn what order would you like the colums of the CSV file?\n" +
                "Please delineate with commas. The options are: " +
                "stars, certificate,"+
                " Duration," +
                " MovieID, Title, and Year.\n\n" +
                "For example, you may write \"Title, Tempo, Duration\"...\n\n" +
                "...or exit by typing 'exit'.\n\n")

            csvAttributeList = re.split('\W+', csvAttributeString)
            for i, v in enumerate(csvAttributeList):
                csvAttributeList[i] = csvAttributeList[i].lower()

            for attribute in csvAttributeList:
                # print "Here is the attribute: " + attribute + " \n"


                if attribute == 'certificate'.lower():
                    csvRowString += 'certificate'
                elif attribute == 'stars'.lower():
                    csvRowString += 'stars'
                elif attribute == 'description'.lower():
                    csvRowString += 'description'
                elif attribute == 'rating'.lower():
                    csvRowString += 'rating'
                elif attribute == 'genre'.lower():
                    csvRowString += 'genre'
                elif attribute == 'duration'.lower():
                    csvRowString += 'duration'
                elif attribute == 'MovieID'.lower():
                    csvRowString += "MovieID"
                elif attribute == 'title'.lower():
                    csvRowString += 'title'
                elif attribute == 'year'.lower():
                    csvRowString += 'year'
                elif attribute == 'Exit'.lower():
                    sys.exit()
                else:
                    prompt = True
                    print ("==============")
                    print ("I believe there has been an error with the input.")
                    print ("==============")
                    break

                csvRowString += ","

            lastIndex = len(csvRowString)
            csvRowString = csvRowString[0:lastIndex-1]
            csvRowString += "\n"
            outputFile1.write(csvRowString);
            csvRowString = ""
    #else, if you want to hard code the order of the csv file and not prompt
    #the user,
    else:
        #################################################
        #change the order of the csv file here
        #Default is to list all available attributes (in alphabetical order)
        csvRowString = ("MovieID,certificate,stars,ArtistID,ArtistLatitude,ArtistLocation,"+
            "ArtistLongitude,ArtistName,Danceability,Duration,KeySignature,"+
            "KeySignatureConfidence,Tempo,TimeSignature,TimeSignatureConfidence,"+
            "Title,Year")
        #################################################

        csvAttributeList = re.split('\W+', csvRowString)
        for i, v in enumerate(csvAttributeList):
            csvAttributeList[i] = csvAttributeList[i].lower()
        outputFile1.write("MovieNumber,");
        outputFile1.write(csvRowString + "\n");
        csvRowString = ""

    #################################################


    #Set the basedir here, the root directory from which the search
    #for files stored in a (hierarchical data structure) will originate
    basedir = "/content/MillionMovieSubset" # "." As the default means the current directory
    ext = ".h5" #Set the extension here. H5 is the extension for HDF5 files.
    #################################################

    print(basedir)

    #FOR LOOP
    for root, dirs, files in os.walk(basedir):
        files = glob.glob(os.path.join(root,'*'+ext))
        for f in files:
            print(f)

            MovieH5File = tables.open_file(f, mode='r')
            Movie = Movie(str(hdf5_getters.get_Movie_id(MovieH5File)))

            # print type(testDanceability)
            # print ("Here is the danceability: ") + str(testDanceability)

            Movie.stars = str(hdf5_getters.get_stars(MovieH5File))
            Movie.duration = str(hdf5_getters.get_duration(MovieH5File))
            # Movie.setgenre()
            # Movie.description = None
            # Movie.rating = None
            Movie.title = str(hdf5_getters.get_title(MovieH5File))
            Movie.year = str(hdf5_getters.get_year(MovieH5File))

            #print Movie count
            csvRowString += str(Movie.MovieCount) + ","

            for attribute in csvAttributeList:
                # print "Here is the attribute: " + attribute + " \n"

                if attribute == 'certificate'.lower():
                    csvRowString += Movie.certificate
                elif attribute == 'stars'.lower():
                    stars = Movie.stars
                    stars = stars.replace(',',"")
                    csvRowString += "\"" + stars + "\""
                elif attribute == 'Duration'.lower():
                    csvRowString += Movie.duration
                elif attribute == 'MovieID'.lower():
                    csvRowString += "\"" + Movie.id + "\""
                elif attribute == 'Title'.lower():
                    csvRowString += "\"" + Movie.title + "\""
                elif attribute == 'Year'.lower():
                    csvRowString += Movie.year
                else:
                    csvRowString += "Erm. This didn't work. Error. :( :(\n"

                csvRowString += ","

            #Remove the final comma from each row in the csv
            lastIndex = len(csvRowString)
            csvRowString = csvRowString[0:lastIndex-1]
            csvRowString += "\n"
            outputFile1.write(csvRowString)
            csvRowString = ""

            MovieH5File.close()

    outputFile1.close()

main()