import ast, inspect, pprint, dis 

def fast_week(): 
    return 7 * 86400

def slow_week(): 
    seconds_per_week = 86400
    return 7 * seconds_per_week


# print the abstract syntax tree 
pprint.pprint(
    ast.dump(
        ast.parse(
            # inspect.getsource will return the source code of a function 
            inspect.getsource(slow_week)
        )
    )
)

tree_root = ast.parse(inspect.getsource(slow_week))
tree_root.body[0]
tree_root.body[0].body


# functions are objects 
slow_week.__code__
slow_week.__code__.co_consts        # show the constands of the function 
slow_week.__code__.co_varnames
slow_week.__code__.co_code

# see the bytecode 
dis.opname[slow_week.__code__.co_code[0]]   # LOAD_CONST
dis.opname[slow_week.__code__.co_code[2]]   # STORE_FAST
dis.opname[slow_week.__code__.co_code[4]]   # LOAT_CONST


print("\n")
dis.dis(slow_week)

'''
(
    "Module(
        body=[
            FunctionDef(
                name='slow_week', 
                decorator_list=[],
                args=arguments(
                    posonlyargs=[], 
                    args=[], kwonlyargs=[], 
                    kw_defaults=[], 
                    defaults=[]
                ),
                body=[
                    Assign(
                        targets=[
                            Name(id='seconds_per_week', ctx=Store())
                        ], 
                        value=Constant(value=86400)
                    ), 
                    Return(
                        value=BinOp(
                            left=Constant(value=7),
                            op=Mult(), 
                            right=Name(id='seconds_per_week', ctx=Load())
                        )
                    )
                ]
            )
        ], 
        type_ignores=[]
    )
)


  3           0 RESUME                   0

  4           2 LOAD_CONST               1 (86400)
              4 STORE_FAST               0 (seconds_per_week)

  5           6 LOAD_CONST               2 (7)
              8 LOAD_FAST                0 (seconds_per_week)
             10 BINARY_OP                5 (*)
             14 RETURN_VALUE



python interpreter: 
    1. read source code 
    2. parse 
    3. generate abstract syntax tree
    4. produce byecode 
    5. run bytecode 



main interpreter stack:
    > each function call pushes a new frame onto this stack 

each frame: 
    > has an evaluation stack (or data stack) and a block stack 


example of above run: 
    1. pusb co_consts[1] to top of evaluation stack 
    2. store top of stack to co_varnames[0]
    3. push co_consts[2] to top of stack 
    4. push value of co_varnames[0] to top of stack 
    5. multiply stack[0] by stack[1], push result to top of stack 
    6. return top of stack 
'''

# code_obj = compile()