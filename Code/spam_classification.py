# Category:    evaluation
# Description: Set a number of learners, split data to train and test set, learn models from train set and estimate classification accuracy on the test set
# Uses:        voting.tab
# Classes:     MakeRandomIndices2
# Referenced:  c_performance.htm

import Orange
from Orange.classification import svm

test_data_size = 25 + 67

def print_classification(classifier, test_data):
    for i in range(test_data_size):
        c = classifier(test_data[i])
        print ("Email ", i, " classified as ", c)

def print_tree0(node, level):
     if not node:
         print (" "*level + "<null node>")
         return
     if node.branch_selector:
        node_desc = node.branch_selector.class_var.name
        node_cont = node.distribution
        print ("\\n" + "   "*level + "%s (%s)" % (node_desc, node_cont),)
        for i in range(len(node.branches)):
            print( "\\n" + "   "*level + ": %s" % node.branch_descriptions[i],)
            print_tree0(node.branches[i], level+1)
     else:
         node_cont = node.distribution
         major_class = node.node_classifier.default_value
         print ("--> %s (%s) " % (major_class, node_cont),)

def print_tree(x):
    if isinstance(x, Orange.classification.tree.TreeClassifier):
        print_tree0(x.tree, 0)
    elif isinstance(x, Orange.classification.tree.Node):
        print_tree0(x, 0)
    else:
        raise (TypeError, "invalid parameter")


# set up the classifiers
train_data = Orange.data.Table("spamTrainingTable.csv")
test_data = Orange.data.Table("spamTestingTable.csv")

bayes_learner = Orange.classification.bayes.NaiveLearner()
bayes_classifier = bayes_learner(train_data)
cn2_rule_learner = Orange.classification.rules.CN2Learner()
cn2_rule_classifier = cn2_rule_learner(train_data)
knnLearner = Orange.classification.knn.kNNLearner()
knnClassifier = knnLearner(train_data)
svm_learner = svm.SVMLearner()
svm_classifier = svm_learner(train_data)
#c45 = Orange.classification.tree.C45Learner(train_data)
tree_learner = Orange.classification.tree.TreeLearner()
tree_classifier = tree_learner(train_data)

print_classification(tree_classifier, test_data)
#print_tree(tree_classifier)
