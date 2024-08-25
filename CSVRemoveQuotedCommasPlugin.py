import sys

class CSVRemoveQuotedCommasPlugin:
    def input(self, inputfile):
        self.infile = open(inputfile, 'r')

    def run(self):
        pass

    def output(self, outputfile):
        outfile = open(outputfile, 'w')
        wholething = self.infile.read()
        quoteflag = False
        for i in range(len(wholething)):
          if (not quoteflag and wholething[i] == '\"'):
            quoteflag = True
          elif (quoteflag and wholething[i] == '\"'):
            quoteflag = False
          if (quoteflag and wholething[i] == ','):
            pass
          else:
            outfile.write(wholething[i])

