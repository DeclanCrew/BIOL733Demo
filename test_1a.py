import glob
import pexpect

test_data = b"actgtgtcagtcagtcg\nttttgggtagctacgat\n"
for attempt in glob.glob("*_assignment_1a.py"):
    child = pexpect.spawn("python3.4 "+attempt)
    with open("logs/" +attempt+".log", "wb") as log:
        child.logfile = log
        child.expect("Enter DNA sequence 1:")
        child.send("actgtgtcagtcagtcg\r")
        child.expect("Enter DNA sequence 2:")
        child.send("ttttgggtagctacgat\r")
        child.expect(pexpect.EOF)

Expectation = [("Enter DNA sequence 1:actgtgtcagtcagtcg", 0),
               ("actgtgtcagtcagtcg", 0),
               ("Enter DNA sequence 2:ttttgggtagctacgat", 0),
               ("ttttgggtagctacgat", 0),
               ("DNA length = 34", 2),
               ("ACTGTGTCAGTCAGTCGTTTTGGGTAGCTACGAT", 2),
               ("Reverse Complement", 0),
               ("ATCGTAGCTACCCAAAACGACTGACTGACACAGT", 3),
               ("RNA length = 41", 4),
               ("ACUGUGUCAGUCAGUCGUUUUGGGUAGCUACGAUAAAAAAA", 4)]

for logf in glob.glob("logs/*.log"):
    print("\t".join(logf.split("_")[:2]))
    score = 0
    with open(logf, "r") as log:
        for line in Expectation:
            logline = log.readline().strip("\r\n")
            if logline == line[0]:
                score += line[1]
            else:
                print("Failure, expected %s, received %s." % (line[0], logline))
    print("Scored %d out of %d" % (score, sum([i[1] for i in Expectation])))
            
            
