# #!/usr/bin/env python3
# # -*- coding: utf-8 -*-
# """
# Created on Tue Dec 10 23:03:28 2019

# @author: kpal
# """

# #!/usr/bin/env python3
# # -*- coding: utf-8 -*-
# """
# Created on Tue Apr 16 16:00:31 2019

# @author: kpal
# """
# import sys
# # sys.path.insert(1, '/src')

# import numpy as np
# import scipy.sparse as sp
# import json
# import model.candidate_collection as cancol
# import model.dataPrep as dp
# import model.sim_var as sc
# import model.SEISA_mod as seps
# import model.structure_lib as util
# from collections import defaultdict
# import time
# import copy



# class Model:


#     def initiate(self, entity_map, list_map, entity_dict, list_dict):

#         self.entity_map = entity_map
#         self.list_map = list_map
#         self.entity_dict = entity_dict
#         self.list_dict = list_dict


#     def calculate(self, domain, query, n_pg = 5, n_p = 6, score_type = 1, category_score_type = 2):

#         print("NPG ",n_pg)
#         self.query = [query]
#         self.n_pg = n_pg
#         self.n_p = n_p

#         self.score_type = score_type
#         self.category_score_type = category_score_type
#         self.domain = domain
#         self.data_path =  domain + "/"

#         # def getTopX(x, arr):

        
#         print("loaded all dictionaries")

#         peergroup_result = defaultdict(list)

#         setup_time = []
#         processing_time = []

#         time_a = time.time()
#         found_list = []
#         peergroupList = []

#         candidates, cl = cancol.candidate_collect(copy.deepcopy(self.query),self.entity_map, self.list_map,2,500)

#         candidate_l = cancol.list_candidate_collect(candidates, self.entity_map)

#         print("PRINTING SOMETHING")
#         print(len(candidate_l))
#         print("Candidates_l : ",candidate_l[0:5])
#         print("Candidates : ",candidates[0:5])


#         entityTolist = (sp.load_npz(self.data_path+"etolist_matrix.npz")).toarray()
#         print("Entity to list size : ", len(entityTolist))
#         print("Entity to list[0] size : ", len(entityTolist[0]))
#         # print(entityTolist[0][0])

#         for i in range(10):
#             print(entityTolist[0][i])

#         print("loaded th matrix")
#         candidate_index, candidate_l_index = [], []

#         for i in candidates:
#             candidate_index.append(self.entity_dict[i])
#         candidate_index.sort()

#         for i in candidate_l:
#             candidate_l_index.append(self.list_dict[i])
#         candidate_l_index.sort()

#         entityTolist = cancol.sliceEtoList(entityTolist, candidate_l_index, candidate_index)

#         entities = [0]*len(candidate_index)
#         print("CAND : ",candidates[:5])

#         seed_inds = []
#         for i in candidates:
#             temp = candidate_index.index(self.entity_dict[i])
#             entities[temp] = i
#             if i in query:
#                 seed_inds.append(temp)

#         print("ENTS : ",entities[:10])

#         group_lists = [0]*len(candidate_l_index)
#         for i in candidate_l:
#             group_lists[candidate_l_index.index(self.list_dict[i])] = i

#         initial_q, q_index = dp.createQuery(self.query, entities)
#         found_peers = []

#         ###############################################


#         c_score = dp.score_dict(self.data_path+"categories_scores.tsv", group_lists,1)
# #        c_score = dp.score_dict(self.data_path+"filtered_categories_scores.tsv", group_lists,1)
#         c_score = np.true_divide(c_score, np.amax(c_score))
# #        e_score = dp.score_dict(self.data_path+"entities_scores.tsv",entities,2)
#         e_score = dp.score_dict(self.data_path+"entities_scores.tsv",entities,self.score_type)
#         e_score = np.true_divide(e_score, np.amax(e_score))
# ##        cat_size = dp.read_size(self.data_path+"categories_score.tsv", group_lists,1)
#         cat_size = dp.score_dict(self.data_path+"categories_scores.tsv", group_lists,self.category_score_type)
#         catsize_norm = np.true_divide(1, cat_size)


#         ###############################################


#         time_b = time.time() - time_a
#         setup_time.append(time_b)
#         time_c = time.time()
#         peer_group = []
#         number_entity = np.shape(entityTolist)[0]
#         S = np.zeros((number_entity, number_entity))

#         # entities => list of E entities, according to the index 
#         # group_lists => list of F facets, according to index

#         print("Entity to list size : ", len(entityTolist))
#         print("Entity to list[0] size : ", len(entityTolist[0]))

#         # Matrix E x F ==> 1 if E belongs in F, 0 otherwise
#         print("Entitytolist : ", entityTolist)

#         # FACET SCORE --> List of (F) scores
#         print("c_score size : ", len(c_score))
#         print("c_score : ", c_score)

#         # ENTITY SCORE --> List of (E) scores 
#         print("e_score size : ", len(e_score))
#         print("e_score : ", e_score)

#         print("Group_lists : ", len(group_lists))
#         print("Group_lists : ", group_lists[:5])

#         print("Query :" , query)
#         print("Initial_q :" , initial_q)



#         #-----------------------------------------------------------
        

#         # print("Entity to list size : ", len(entityTolist))
#         # print("Entitytolist : ", entityTolist)
#         # print(len(entityTolist))


#         # for i in range(self.n_pg):
#         #     print("done creating s matrix")
#         #     D = dp.createdismatrix(S)
#         #     print("done creating d matrix")
#         #     peer_group, c_index, group_score = seps.findGroup_Listconst_discomp_score(initial_q, S, self.n_p, entityTolist, found_peers, D, self.list_map, group_lists, catsize_norm, found_list)

#         #     group = []
#         #     for j in peer_group:
#         #         if ((j in found_peers)!= True):
#         #             found_peers.append(j)
#         #         group.append(entities[j])

#         #     common_list = dp.updateMatrix(group, self.query, entityTolist, entities)
#         #     peer_lists = []
#         #     for j in common_list:
#         #         peer_lists.append(group_lists[j])

#         #     g = util.PeerGroup()
#         #     g.initiate(i, group, peer_lists, group_score[0], group_score[1], group_score[2], group_lists[c_index])
#         #     peergroupList.append(g)

#         alpha = 0.3
#         beta = 0.3
#         gamma = 0.4

#         relMat = np.around(sc.createSimMatrix(entityTolist, S, c_score, e_score, []), decimals = 2)
        

#         # entity_dict
#         entityTolistC = np.zeros((len(entityTolist), len(entityTolist[0])))
#         entityTolistI = []

#         print("SEED INDS : ", seed_inds)
#         print(entities[seed_inds[0]])
#         for i in seed_inds:
#             for k in range(len(c_score)):
#                 for j in range(len(e_score)):
#                     if(entityTolist[j][k] == 1):
#                         entityTolistC[j][k] += alpha * relMat[i][j] 

#         cnt = 0
#         for i in range(len(e_score)):
#             if(entityTolistC[i][seed_inds[0]] > 0):
#                 cnt += 1 

#         print("CNT", cnt)
#         print("ENTITY TO LIST : ", entityTolistC)
#         print("RELMAT : ",relMat)
#         peerGroups = []

#         # Storing Score, Index for every entity in facets (to sort)`
#         # for k in range(len(c_score)):
#         #     lists = []
#         #     for j in range(len(e_score)):
#         #         lists.append([entityTolistC[j][k], j])
#         #     entityTolistI.append(lists)

#         x = 5

#         cnt = 0

#         # -------------------------------- ALGORITHM 2 --------------------
        
#         # STEP 1-2
#         # STEP FOR FINDING HIGH x SCORES FOR EACH FACET
#         peerGroups = []
#         for j in range(len(c_score)):        
#             inds = set()
#             inds_1 = []
#             for i in range(x):
#                 mini = -1
#                 for k in range(len(e_score)):
#                     if(k in inds_1):
#                         continue
#                     if(entityTolistC[k][j] > mini):
#                         ind = k 
#                         mini = entityTolistC[k][j]
#                 inds.add(tuple([-1 * mini, ind]))
#                 inds_1.append(ind)

#             peerGroups.append(inds)

#         # STEP 3-5
#         for k in range(len(c_score)):
#             for j in range(len(e_score)):
#                 for i in peerGroups[k]:
#                     entityTolist[j][k] += beta * relMat[j][i[1]]

#         # STEP 6-7
#         peerGroups = []
#         for j in range(len(c_score)):        
#             inds = set()
#             inds_1 = []
#             for i in range(x):
#                 mini = -1
#                 for k in range(len(e_score)):
#                     if(k in inds_1):
#                         continue
#                     if(entityTolistC[k][j] > mini):
#                         ind = k 
#                         mini = entityTolistC[k][j]
#                 inds.add(tuple([-1 * mini, ind]))
#                 inds_1.append(ind)

#             peerGroups.append(inds)

#         # STEP 8-12
#         for i in range(len(c_score)):
#             for k in peerGroups[i]:
#                 for j in range(len(c_score)):
#                     if(i == j):
#                         continue 
#                     for k1 in peerGroups[j]:
#                         entityTolistC[k[1]][i] -= gamma * relMat[k1[1]][k[1]]

#         # Calculating Group Score
#         groupScores = []
#         cunt = 0
#         for i in range(len(c_score)):
#             sm = 0
#             for j in peerGroups[i]:
#                 sm += entityTolistC[j[1]][i]
#             if sm == 0:
#                 cunt += 1
#             groupScores.append(sm)

#         print("BAD ", cunt)
#         print(groupScores)
#         #  To store top k groups
#         topGroups = set()
#         tgInd = set()
#         for _ in range(n_pg):
#             mex = -10000000
#             for i in range(len(c_score)):
#                 if(i in tgInd):
#                     continue
#                 if(groupScores[i] > mex):
#                     ind = i
#                     mex = groupScores[i]
#             topGroups.add(tuple([-1*mex, ind]))
#             tgInd.add(ind)

#         print("PRINTING TOP K GROUPS ITER 1 ", len(topGroups))
#         for i in topGroups:
#             print(group_lists[i[1]])



#         # DEBUGGING FOR CHECKING peerGroups

#         # cnt = 0
#         # for i in peerGroups:
#         #     # print(i)
#         #     # if(i[0])
#         #     # print("Starting Peer", len(i))
#         #     if (next(iter(i))[0] == 0):
#         #         print(group_lists[cnt])
#         #     # for j in i:
#         #     cnt += 1
#             #     if(j[0] == 0):

#             #         break
#                 # print(entities[j[1]])
#             # print("Ending Peer")




#         print("done calculating peer group")
#         # peergroup_result[self.query[0]] = [peergroupList]
#         peergroup_result[self.query[0]] = []

#         time_d = time.time() - time_c
#         processing_time.append(time_d)

#         count = 0
#         for i in setup_time:
#             count += i
#         print("avg setup time: ", count / len(self.query))

#         count = 0
#         for i in processing_time:
#             count += i
#         print("avg setup time: ", count / len(self.query))

#         return peergroup_result
    
#         # STEP - 0 : Ma'am's stuff
#         # STEP - 1 : p*l Entities of candidate_l
#         # STEP - 2 : Create our own SimMatrix using rel score 
#        

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 23:03:28 2019
 
@author: kpal
"""
 
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 16:00:31 2019
 
@author: kpal
"""
import sys
# sys.path.insert(1, '/src')
 
import numpy as np
import scipy.sparse as sp
import json
import model.candidate_collection as cancol
import model.dataPrep as dp
import model.sim_var as sc
import model.SEISA_mod as seps
import model.structure_lib as util
from collections import defaultdict
import time
import copy
 
 
 
class Model:
 
 
    def initiate(self, entity_map, list_map, entity_dict, list_dict):
 
        self.entity_map = entity_map
        self.list_map = list_map
        self.entity_dict = entity_dict
        self.list_dict = list_dict
 
 
    def calculate(self, domain, query, n_pg = 5, n_p = 6, score_type = 1, category_score_type = 2):
 
        print("NPG ",n_pg)
        self.query = [query]
        self.n_pg = n_pg
        self.n_p = n_p
 
        self.score_type = score_type
        self.category_score_type = category_score_type
        self.domain = domain
        self.data_path =  domain + "/"
 
        # def getTopX(x, arr):
 
 
        print("loaded all dictionaries")
 
        peergroup_result = defaultdict(list)
 
        setup_time = []
        processing_time = []
 
        time_a = time.time()
        found_list = []
        peergroupList = []
 
        candidates, cl = cancol.candidate_collect(copy.deepcopy(self.query),self.entity_map, self.list_map,2,2000)
 
        candidate_l = cancol.list_candidate_collect(candidates, self.entity_map)
 
        print("PRINTING SOMETHING")
        print(len(candidate_l))
        print("Candidates_l : ",candidate_l[0:5])
        print("Candidates : ",candidates[0:5])
 
 
        entityTolist = (sp.load_npz(self.data_path+"etolist_matrix.npz")).toarray()
       

        print("Entity to list size : ", len(entityTolist))
        print("Entity to list[0] size : ", len(entityTolist[0]))
        # print(entityTolist[0][0])
 
        for i in range(10):
            print(entityTolist[0][i])
 
        print("loaded th matrix")
        candidate_index, candidate_l_index = [], []
 
        for i in candidates:
            candidate_index.append(self.entity_dict[i])
        candidate_index.sort()
 
        for i in candidate_l:
            candidate_l_index.append(self.list_dict[i])
        candidate_l_index.sort()
 
 #        [[0.174 0.174 0.174 0.174 0.174 0.    0.    0.    0.    0.    0.    0.
 #  0.    0.    0.    0.    0.   ]
 # [0.    0.    0.    0.    0.    0.    0.    0.    0.    0.    0.    0.
 #  0.    0.    0.    0.    0.   ]
 # [0.    0.171 0.    0.    0.    0.    0.    0.    0.    0.    0.    0.
 #  0.    0.171 0.171 0.    0.   ]
 # [0.165 0.165 0.    0.    0.165 0.    0.    0.    0.    0.    0.    0.
 #  0.    0.    0.    0.    0.   ]
 # [0.    0.162 0.    0.    0.    0.162 0.    0.    0.    0.162 0.    0.
 #  0.    0.    0.    0.    0.   ]
 # [0.174 0.    0.    0.    0.    0.    0.174 0.174 0.    0.    0.174 0.174
 #  0.    0.    0.    0.    0.   ]
 # [0.    0.    0.    0.    0.    0.    0.183 0.183 0.    0.    0.183 0.
 #  0.    0.    0.    0.    0.   ]
 # [0.171 0.    0.    0.    0.    0.    0.171 0.171 0.    0.    0.    0.
 #  0.    0.    0.    0.    0.171]
 # [0.    0.    0.    0.    0.    0.    0.    0.129 0.    0.    0.    0.
 #  0.129 0.    0.    0.129 0.   ]]

        entities = [0]*len(candidate_index)
        print("CAND : ",candidates[:5])
 
        seed_inds = []
        for i in candidates:
            temp = candidate_index.index(self.entity_dict[i])
            entities[temp] = i
            if i in query:
                seed_inds.append(temp)
 
        print("ENTS : ",entities[:10])
 
        group_lists = [0]*len(candidate_l_index)
        for i in candidate_l:
            group_lists[candidate_l_index.index(self.list_dict[i])] = i
 
        initial_q, q_index = dp.createQuery(self.query, entities)
        found_peers = []


        # TOY SET, create own entity to list

        # UNCOMMENT BELOW LINES FOR TOY
        # ----------------------
        # entityTolist = []

        # for j in range(len(candidates)):
        #     temp = []
        #     for i in range(len(candidate_l)):
        #         if(entities[j] in self.list_map[group_lists[i]]):
        #             temp.append(1)
        #         else:
        #             temp.append(0)
        #     entityTolist.append(temp)
        #------------------------------


        # COMMENT BELOW LINES FOR TOY
        # ----------------------------
        entityTolist = cancol.sliceEtoList(entityTolist, candidate_l_index, candidate_index)
        # ----------------------------
        # print("ENTTOLIST : ", entityTolist)


         # [0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] - JFK
         # [0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0] - ABE
         # [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0] - FDG
         # [1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] - DRS
         # [0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0] - GRR
         # [0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0] - HSB
         # [0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0] - MPL
         # [0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1] - OTT
         # [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0] - KIR

 
        ###############################################
 
 
        c_score = dp.score_dict(self.data_path+"categories_scores.tsv", group_lists,1)
#        c_score = dp.score_dict(self.data_path+"filtered_categories_scores.tsv", group_lists,1)
        c_score = np.true_divide(c_score, np.amax(c_score))
#        e_score = dp.score_dict(self.data_path+"entities_scores.tsv",entities,2)
        e_score = dp.score_dict(self.data_path+"entities_scores.tsv",entities,self.score_type)
        e_score = np.true_divide(e_score, np.amax(e_score))
##        cat_size = dp.read_size(self.data_path+"categories_score.tsv", group_lists,1)
        cat_size = dp.score_dict(self.data_path+"categories_scores.tsv", group_lists,self.category_score_type)
        catsize_norm = np.true_divide(1, cat_size)
 
 
        ###############################################
 
 
        time_b = time.time() - time_a
        setup_time.append(time_b)
        time_c = time.time()
        peer_group = []
        number_entity = np.shape(entityTolist)[0]
        S = np.zeros((number_entity, number_entity))
 
        # entities => list of E entities, according to the index 
        # group_lists => list of F facets, according to index
 
        print("Entity to list size : ", len(entityTolist))
        print("Entity to list[0] size : ", len(entityTolist[0]))
 
        # Matrix E x F ==> 1 if E belongs in F, 0 otherwise
        print("Entitytolist : ", entityTolist)
 
        # FACET SCORE --> List of (F) scores
        print("c_score size : ", len(c_score))
        print("c_score : ", c_score)
 
        # ENTITY SCORE --> List of (E) scores 
        print("e_score size : ", len(e_score))
        print("e_score : ", e_score)
 
        print("Group_lists : ", len(group_lists))
        print("Group_lists : ", group_lists[:5])
 
        print("Query :" , query)
        print("Initial_q :" , initial_q)
 
 
 
        #-----------------------------------------------------------
 
 
        # print("Entity to list size : ", len(entityTolist))
        # print("Entitytolist : ", entityTolist)
        # print(len(entityTolist))
 
 
        # for i in range(self.n_pg):
        #     print("done creating s matrix")
        #     D = dp.createdismatrix(S)
        #     print("done creating d matrix")
        #     peer_group, c_index, group_score = seps.findGroup_Listconst_discomp_score(initial_q, S, self.n_p, entityTolist, found_peers, D, self.list_map, group_lists, catsize_norm, found_list)
 
        #     group = []
        #     for j in peer_group:
        #         if ((j in found_peers)!= True):
        #             found_peers.append(j)
        #         group.append(entities[j])
 
        #     common_list = dp.updateMatrix(group, self.query, entityTolist, entities)
        #     peer_lists = []
        #     for j in common_list:
        #         peer_lists.append(group_lists[j])
 
        #     g = util.PeerGroup()
        #     g.initiate(i, group, peer_lists, group_score[0], group_score[1], group_score[2], group_lists[c_index])
        #     peergroupList.append(g)

        # for i in range(len(e_score)):
        #     print(entities[i])

        # for i in range(len(c_score)):
        #     print(group_lists[i])

        print()

 
        alpha = 0.5
        beta = 0.1
        gamma = 0.4
 
        relMat = np.around(sc.createSimMatrix(entityTolist, S, c_score, e_score, []), decimals = 2)
        

        
        # RELMAT :  [[1.  0.59 0.6  0.57 0.56 0.42 0.4  0.35 0.34]
                #   [0.59 1.   0.57 0.55 0.54 0.61 0.61 0.58 0.43]
                #   [0.6  0.57 1.   0.72 0.68 0.47 0.46 0.41 0.4 ]
                #   [0.57 0.55 0.72 1.   0.65 0.48 0.46 0.41 0.4 ]
                #   [0.56 0.54 0.68 0.65 1.   0.48 0.47 0.42 0.4 ]
                #   [0.42 0.61 0.47 0.48 0.48 1.   0.77 0.76 0.54]
                #   [0.4  0.61 0.46 0.46 0.47 0.77 1.   0.8  0.56]
                #   [0.35 0.58 0.41 0.41 0.42 0.76 0.8  1.   0.63]
                #   [0.34 0.43 0.4  0.4  0.4  0.54 0.56 0.63 1.  ]]


        # entity_dict
        entityTolistC = np.zeros((len(entityTolist), len(entityTolist[0])))
        # entityTolistI = []
 
        print("SEED INDS : ", seed_inds)
        print(entities[seed_inds[0]])
        for i in seed_inds:
            for k in range(len(c_score)):
                for j in range(len(e_score)):
                    if(j in seed_inds):
                        continue

                    if(entityTolist[j][k] == 1):
                        # print(entities[j], group_lists[k])
                        entityTolistC[j][k] += ((alpha * relMat[i][j])/len(seed_inds))
 
 
 
        # cnt = 0
        # for i in range(len(e_score)):
        #     if(entityTolistC[i][seed_inds[0]] > 0):
        #         cnt += 1 
 
        # print("CNT", cnt)
        print("ENTITY TO LIST : ", entityTolistC)
        print("RELMAT : ",relMat)
        peerGroups = [0]*len(c_score)
 
 
        x = 2
        # groupScores = []
        cnt = 0
 
        # -------------------------------- ALGORITHM 2 --------------------
 
        # STEP 1-2
        # STEP FOR FINDING HIGH x SCORES FOR EACH FACET
        for j in range(len(c_score)):        
            inds = set()
            inds_1 = []
            for i in range(x):
                mini = -100000000
                for k in range(len(e_score)):
                    if(k in inds_1):
                        continue
                    if(entityTolistC[k][j] > mini):
                        ind = k 
                        mini = entityTolistC[k][j]
                if(mini != 0):
                    inds.add(tuple([mini, ind]))
                    inds_1.append(ind)
 
            peerGroups[j] = inds
 
        print("AFTER ALPHA ADDITION")
        # print(peerGroups[:10])
 
        print("Time:", time.time() - time_c)
        time_c = time.time()
 
        # Calculating Group Score
        groupScores = []
        print("Top K groups")
        for i in range(len(c_score)):
            sm = 0
            for j in peerGroups[i]:
                # sm += entityTolistC[j[1]][i]
                sm += j[0]
            groupScores.append(sm)
 
        topGroups = []
        tgInd = set()
        for _ in range(len(c_score)):
            mex = -1000000000
            for i in range(len(c_score)):
                if(i in tgInd):
                    continue
                if(groupScores[i] > mex):
                    ind = i
                    mex = groupScores[i]
            topGroups.append([mex, ind])
            tgInd.add(ind)
 
        topGroups = sorted(topGroups, reverse=True)
        print(topGroups[:n_pg])
        for i in topGroups[:n_pg]:
            print(group_lists[i[1]], i[0])
            # print(peerGroups[i[1]])
            for j in peerGroups[i[1]]:
                print(entities[j[1]], j[0])
            print()

 
        # STEP 3-5
        betaScores = np.zeros((len(entityTolist), len(entityTolist[0])))
        counts = np.zeros((len(entityTolist), len(entityTolist[0])))

        # for k in topGroups:
        #     for j in range(len(e_score)):
        #         if(j in seed_inds):
        #                 continue
        #         for i in peerGroups[k[1]]:
        #             if(i[1] == j):
        #                 continue
                    
        #             if(entityTolist[j][k[1]] == 1):
        #                 # if(k[1] == 1147):
        #                 #     print(entities[j], entities[i[1]], group_lists[k[1]])
        #                 #     print("ADDING")
        #                 #     print(relMat[j][i[1]])
        #                 # if(k[1] == 1077):
        #                 #     print(entities[j], entities[i[1]], group_lists[k[1]])
        #                 #     print("ADDING")
        #                 #     print(relMat[j][i[1]])
        #                 betaScores[j][k[1]] += ((beta * (relMat[j][i[1]])))
        #                 counts[j][k[1]] += 1

        for k in topGroups[:1000]:
            for j in peerGroups[k[1]]:
                # if(j in seed_inds):
                #         continue
                for i in peerGroups[k[1]]:
                    if(i[1] == j[1]):
                        continue
                    
                    # if(entityTolist[j][k[1]] == 1):
                    if(k[1] == 1147):
                        print(entities[j[1]], entities[i[1]], group_lists[k[1]])
                        print("ADDING")
                        print(relMat[j[1]][i[1]])
                    if(k[1] == 1077):
                        print(entities[j[1]], entities[i[1]], group_lists[k[1]])
                        print("ADDING")
                        print(relMat[j[1]][i[1]])
                    # betaScores[j][k[1]] += ((beta * (relMat[j][i[1]])))
                        # counts[j][k[1]] += 1
                    # if(k[1] == 1147):
                    #     print("adding ", entities[j[1]], entities[i[1]], relMat[j[1]][i[1]])
                    groupScores[k[1]] += ((beta*(relMat[j[1]][i[1]]))/2 * x)




        # for i in range(len(e_score)):
        #     for j in topGroups:
        #         if(counts[i][j[1]] != 0):
        #             if(entityTolist[i][j[1]] == 1):
        #                 entityTolistC[i][j[1]] += (betaScores[i][j[1]]/counts[i][j[1]])

                    # entityTolistC[j][k[1]] += ((beta * (relMat[j][i[1]]))/divi)
 
 
        # STEP 6-7
        # peerGroups = [0]*len(c_score)
        # for j in topGroups:        
        #     inds = set()
        #     inds_1 = []
        #     for i in range(x):
        #         mini = -1
        #         for k in range(len(e_score)):
        #             if(k in inds_1):
        #                 continue
        #             if(entityTolistC[k][j[1]] > mini):
        #                 ind = k 
        #                 mini = entityTolistC[k][j[1]]
        #         if(mini != 0):
        #             inds.add(tuple([mini, ind]))
        #             inds_1.append(ind)
 
 
        #     peerGroups[j[1]] = inds


        print("AFTER BETA ADDITION")
        # print(peerGroups[:10])
        # print("PRINTING TOP K GROUPS ITER 1 ", len(topGroups))
        # for i in topGroups[:10]:
        #     print(group_lists[i[1]], i[0])
        #     # print(peerGroups[i[1]])
        #     for j in peerGroups[i[1]]:
        #         print(entities[j[1]], j[0])
        #     print()
 
        print("Time:", time.time() - time_c)
        time_c = time.time()
 
        # Calculating Group Score
        # groupScores = []
        print("Top K groups")
        # for i in topGroups:
        #     sm = 0
        #     for j in peerGroups[i[1]]:
        #         # sm += entityTolistC[j[1]][i]
        #         sm += j[0]
        #     groupScores[i[1]] = sm
 
        topGroups_new = []
        tgInd = set()
        for _ in range(len(c_score)):
            mex = -1000000000
            for i in topGroups:
                if(i[1] in tgInd):
                    continue
                if(groupScores[i[1]] > mex):
                    ind = i[1]
                    mex = groupScores[i[1]]
            topGroups_new.append([mex, ind])
            tgInd.add(ind)
 
        topGroups_new = sorted(topGroups_new, reverse=True)


        print(topGroups_new[:n_pg])
        topGroups = copy.deepcopy(topGroups_new)
        for i in topGroups[:n_pg]:
            print(group_lists[i[1]], i[0])
            # print(peerGroups[i[1]])
            for j in peerGroups[i[1]]:
                print(entities[j[1]], j[0])
            print()
 
        print("PRINTING SOMETHING")
        print(group_lists[1077])
        print( topGroups[1082][0])
        for j in peerGroups[1077]:
            print(entities[j[1]], j[0])
        print()
        # STEP 8-12
        # for i in topGroups:
        #     for k in peerGroups[i[1]]:
        #         if(k[1] in seed_inds):
        #             continue
        #         for j in topGroups:
        #             if(i[1] == j[1]):
        #                 continue 
        #             for k1 in peerGroups[j[1]]:
        #                 # if(k1[1] == k[1]):
        #                 #     continue
        #                 # entityTolistC[k[1]][i[1]] -= ((gamma * relMat[k1[1]][k[1]])/((len(topGroups)-1)*x))
        #                 groupScores[i[1]] -= ((gamma * relMat[k1[1]][k[1]])/((len(topGroups)-1)*x))

        topGroups = []
        topGroups.append(topGroups_new[0])
        done_set = set()
        done_set.add(topGroups[0][1])

        print("TopGroups : ", topGroups)
        # print(topGroups_new)
        # for i in topGroups_new:
        #     print(len(i))

        for i in range(n_pg - 1):
            top_score = -100000
            ind_to_add = -1            
            for j in topGroups_new:
                if j[1] in done_set:
                    continue
                temp = 0
                count = 0
                for ent in peerGroups[j[1]]:
                    for k in topGroups:
                        for ents in peerGroups[k[1]]:
                            # print(group_lists[j[1]], group_lists[k[1]])
                            # print(entities[ent[1]], entities[ents[1]])
                            temp -= gamma * (relMat[ent[1]][ents[1]])
                            count += 1

                # print(count)
                if(count == 0):
                    print("Count = 0 for", group_lists[j[1]])
                    continue
                if((j[0] + ((temp)/count)) > top_score):
                    top_score = j[0] + ((temp)/count)
                    ind = j[1]

            print("Chose next facet", group_lists[ind])
            print("Score Obtained : ", top_score)
            topGroups.append([top_score, ind])
            done_set.add(ind)


 
#         peerGroups = [0]*len(c_score)
#         for j in topGroups:        
#             inds = set()
#             inds_1 = []
#             for i in range(x):
#                 mini = -1
#                 for k in range(len(e_score)):
#                     if(k in inds_1):
#                         continue
#                     if(entityTolistC[k][j[1]] > mini):
#                         ind = k 
#                         mini = entityTolistC[k][j[1]]
#                 if(mini != 0):
#                     inds.add(tuple([mini, ind]))
#                     inds_1.append(ind)
 
 
#             peerGroups[j[1]] = inds

#         print("AFTER GAMMA ADDITION")
#         print(peerGroups[:10])
 
#         print("Time:", time.time() - time_c)
#         time_c = time.time()
 
# # /(x*(len(peerGroups)-1))
#         # Calculating Group Score
#         # groupScores = []
#         for i in topGroups:
#             sm = 0
#             for j in peerGroups[i[1]]:
#                 # sm += entityTolistC[j[1]][i]
#                 sm += j[0]
#             groupScores[i[1]] = sm
 
        print("GROUP SCORES :")
        # print(groupScores)
        #  To store top k groups
        # topGroups_new = []
        # tgInd = set()
        # for _ in range(len(c_score)):
        #     mex = -1000000000
        #     for i in topGroups:
        #         if(i[1] in tgInd):
        #             continue
        #         if(groupScores[i[1]] > mex):
        #             ind = i[1]
        #             mex = groupScores[i[1]]
        #     topGroups_new.append(tuple([mex, ind]))
        #     tgInd.add(ind)
 
        # topGroups_new = sorted(topGroups_new, reverse=True)

        # topGroups = copy.deepcopy(topGroups_new)
        # print(topGroups[:n_pg])
        print("PRINTING TOP K GROUPS ITER 1 ", len(topGroups))
        for i in topGroups:
            print(group_lists[i[1]], i[0])
            # print(peerGroups[i[1]])
            for j in peerGroups[i[1]]:
                print(entities[j[1]], j[0])
            print()
 
 
 
        # DEBUGGING FOR CHECKING peerGroups
 
        # cnt = 0
        # for i in peerGroups:
        #     # print(i)
        #     # if(i[0])
        #     # print("Starting Peer", len(i))
        #     if (next(iter(i))[0] == 0):
        #         print(group_lists[cnt])
        #     # for j in i:
        #     cnt += 1
            #     if(j[0] == 0):
 
            #         break
                # print(entities[j[1]])
            # print("Ending Peer")
 
 
 
 
        print("done calculating peer group")
        # peergroup_result[self.query[0]] = [peergroupList]
        peergroup_result[self.query[0]] = []
 
        time_d = time.time() - time_c
        processing_time.append(time_d)
 
        count = 0
        for i in setup_time:
            count += i
        print("avg setup time: ", count / len(self.query))
 
        count = 0
        for i in processing_time:
            count += i
        print("avg setup time: ", count / len(self.query))
 
        return peergroup_result
 
       #---------------------------------------------------------
       # IBM
        # type+wikicat_Publicly_traded_companies_of_the_United_States
        # type+wikicat_Electronics_companies_of_the_United_States
        # type+wikicat_Companies_in_the_Dow_Jones_Industrial_Average
        # type+wordnet_company_108058098
        # type+wikicat_Software_companies_of_the_United_States
        # done calculating peer group
        # avg setup time:  0.2951045036315918
        # avg setup time:  29.955456256866455
        # -------------------------------------------------------


        """
        1. Toy Example - alpha = 0.3, beta = 0.3, gamma = 0.4
        2. Explain problem with beta = 0.3 (George Clooney, Actors from Kentucky), 
        3. Change beta = 0.10, show results
        4. Change 1500 -> 100
        5. Wasn't able to do much for gamma
        """

        # MMR Algo
