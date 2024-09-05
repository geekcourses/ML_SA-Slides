# # GIVEN:
# 60% male 		=> Product 1
# 40% female 	=> Product 2
# Among female customers, 30% choose Product1, while 70% choose Product2.

# TASK:
# Find the probability of a client to choose Product1, given that the client is male


# Solution
A - client choose Product1
B - the client is male


P(A|B) = P(A and B) / P(B),

P(B) = 50%,
P(A and B) is the probability of a male customer choosing Product A. This is given to us as 60%.

Therefor, <code>P(A|B) = P(A and B) / P(B) = 0.3 / 0.5 = 0.6</code>