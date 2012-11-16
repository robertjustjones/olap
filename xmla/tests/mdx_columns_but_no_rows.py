"""
select [Gender].[Gender].ALLMEMBERS on columns from [Sales]

"""

result={'Axes': {'Axis': {'Tuples': {'Tuple': [{'Member': {'Caption': 'F',
                                                    'DisplayInfo': '0',
                                                    'LName': '[Gender].[Gender]',
                                                    'LNum': '1',
                                                    'UName': '[Gender].[F]',
                                                    '_Hierarchy': 'Gender'}},
                                        {'Member': {'Caption': 'M',
                                                    'DisplayInfo': '131072',
                                                    'LName': '[Gender].[Gender]',
                                                    'LNum': '1',
                                                    'UName': '[Gender].[M]',
                                                    '_Hierarchy': 'Gender'}}]},
                   '_name': 'Axis0'}},
 'CellData': {'Cell': [{'FmtValue': '131.558',
                        'FormatString': 'Standard',
                        'Value': 131558.0,
                        '_CellOrdinal': '0'},
                       {'FmtValue': '135.215',
                        'FormatString': 'Standard',
                        'Value': 135215.0,
                        '_CellOrdinal': '1'}]},
 'OlapInfo': {'AxesInfo': {'AxisInfo': {'HierarchyInfo': {'Caption': {'_name': '[Gender].[MEMBER_CAPTION]'},
                                                          'DisplayInfo': {'_name': '[Gender].[DISPLAY_INFO]'},
                                                          'LName': {'_name': '[Gender].[LEVEL_UNIQUE_NAME]'},
                                                          'LNum': {'_name': '[Gender].[LEVEL_NUMBER]'},
                                                          'UName': {'_name': '[Gender].[MEMBER_UNIQUE_NAME]'},
                                                          '_name': 'Gender'},
                                        '_name': 'Axis0'}},
              'CellInfo': {'FmtValue': {'_name': 'FORMATTED_VALUE'},
                           'FormatString': {'_name': 'FORMAT_STRING'},
                           'Value': {'_name': 'VALUE'}},
              'CubeInfo': {'Cube': {'CubeName': 'Sales'}}},
 'schema': {'_elementFormDefault': 'qualified',
            '_targetNamespace': 'urn:schemas-microsoft-com:xml-analysis:mddataset',
            'complexType': [{'_name': 'MemberType',
                             'attribute': {'_name': 'Hierarchy',
                                           '_type': 'xsd:string'},
                             'sequence': {'element': [{'_name': 'UName',
                                                       '_type': 'xsd:string'},
                                                      {'_name': 'Caption',
                                                       '_type': 'xsd:string'},
                                                      {'_name': 'LName',
                                                       '_type': 'xsd:string'},
                                                      {'_name': 'LNum',
                                                       '_type': 'xsd:unsignedInt'},
                                                      {'_name': 'DisplayInfo',
                                                       '_type': 'xsd:unsignedInt'}],
                                          'sequence': {'_maxOccurs': 'unbounded',
                                                       '_minOccurs': '0',
                                                       'any': {'_maxOccurs': 'unbounded',
                                                               '_processContents': 'lax'}}}},
                            {'_name': 'PropType',
                             'attribute': {'_name': 'name',
                                           '_type': 'xsd:string'}},
                            {'_name': 'TupleType',
                             'sequence': {'_maxOccurs': 'unbounded',
                                          'element': {'_name': 'Member',
                                                      '_type': 'MemberType'}}},
                            {'_name': 'MembersType',
                             'attribute': {'_name': 'Hierarchy',
                                           '_type': 'xsd:string'},
                             'sequence': {'_maxOccurs': 'unbounded',
                                          'element': {'_name': 'Member',
                                                      '_type': 'MemberType'}}},
                            {'_name': 'TuplesType',
                             'sequence': {'_maxOccurs': 'unbounded',
                                          'element': {'_name': 'Tuple',
                                                      '_type': 'TupleType'}}},
                            {'_name': 'CrossProductType',
                             'attribute': {'_name': 'Size',
                                           '_type': 'xsd:unsignedInt'},
                             'sequence': {'choice': {'_maxOccurs': 'unbounded',
                                                     '_minOccurs': '0',
                                                     'element': [{'_name': 'Members',
                                                                  '_type': 'MembersType'},
                                                                 {'_name': 'Tuples',
                                                                  '_type': 'TuplesType'}]}}},
                            {'_name': 'OlapInfo',
                             'sequence': {'element': [{'_name': 'CubeInfo',
                                                       'complexType': {'sequence': {'element': {'_maxOccurs': 'unbounded',
                                                                                                '_name': 'Cube',
                                                                                                'complexType': {'sequence': {'element': {'_name': 'CubeName',
                                                                                                                                         '_type': 'xsd:string'}}}}}}},
                                                      {'_name': 'AxesInfo',
                                                       'complexType': {'sequence': {'element': {'_maxOccurs': 'unbounded',
                                                                                                '_name': 'AxisInfo',
                                                                                                'complexType': {'attribute': {'_name': 'name',
                                                                                                                              '_type': 'xsd:string'},
                                                                                                                'sequence': {'element': {'_maxOccurs': 'unbounded',
                                                                                                                                         '_minOccurs': '0',
                                                                                                                                         '_name': 'HierarchyInfo',
                                                                                                                                         'complexType': {'attribute': {'_name': 'name',
                                                                                                                                                                       '_type': 'xsd:string',
                                                                                                                                                                       '_use': 'required'},
                                                                                                                                                         'sequence': {'sequence': [{'_maxOccurs': 'unbounded',
                                                                                                                                                                                    'element': [{'_name': 'UName',
                                                                                                                                                                                                 '_type': 'PropType'},
                                                                                                                                                                                                {'_name': 'Caption',
                                                                                                                                                                                                 '_type': 'PropType'},
                                                                                                                                                                                                {'_name': 'LName',
                                                                                                                                                                                                 '_type': 'PropType'},
                                                                                                                                                                                                {'_name': 'LNum',
                                                                                                                                                                                                 '_type': 'PropType'},
                                                                                                                                                                                                {'_maxOccurs': 'unbounded',
                                                                                                                                                                                                 '_minOccurs': '0',
                                                                                                                                                                                                 '_name': 'DisplayInfo',
                                                                                                                                                                                                 '_type': 'PropType'}]},
                                                                                                                                                                                   {'any': {'_maxOccurs': 'unbounded',
                                                                                                                                                                                            '_minOccurs': '0',
                                                                                                                                                                                            '_processContents': 'lax'}}]}}}}}}}}},
                                                      {'_name': 'CellInfo',
                                                       'complexType': {'sequence': {'sequence': [{'_maxOccurs': 'unbounded',
                                                                                                  '_minOccurs': '0',
                                                                                                  'choice': {'element': [{'_name': 'Value',
                                                                                                                          '_type': 'PropType'},
                                                                                                                         {'_name': 'FmtValue',
                                                                                                                          '_type': 'PropType'},
                                                                                                                         {'_name': 'BackColor',
                                                                                                                          '_type': 'PropType'},
                                                                                                                         {'_name': 'ForeColor',
                                                                                                                          '_type': 'PropType'},
                                                                                                                         {'_name': 'FontName',
                                                                                                                          '_type': 'PropType'},
                                                                                                                         {'_name': 'FontSize',
                                                                                                                          '_type': 'PropType'},
                                                                                                                         {'_name': 'FontFlags',
                                                                                                                          '_type': 'PropType'},
                                                                                                                         {'_name': 'FormatString',
                                                                                                                          '_type': 'PropType'},
                                                                                                                         {'_name': 'NonEmptyBehavior',
                                                                                                                          '_type': 'PropType'},
                                                                                                                         {'_name': 'SolveOrder',
                                                                                                                          '_type': 'PropType'},
                                                                                                                         {'_name': 'Updateable',
                                                                                                                          '_type': 'PropType'},
                                                                                                                         {'_name': 'Visible',
                                                                                                                          '_type': 'PropType'},
                                                                                                                         {'_name': 'Expression',
                                                                                                                          '_type': 'PropType'}]}},
                                                                                                 {'_maxOccurs': 'unbounded',
                                                                                                  '_minOccurs': '0',
                                                                                                  'any': {'_maxOccurs': 'unbounded',
                                                                                                          '_processContents': 'lax'}}]}}}]}},
                            {'_name': 'Axes',
                             'sequence': {'_maxOccurs': 'unbounded',
                                          'element': {'_name': 'Axis',
                                                      'complexType': {'attribute': {'_name': 'name',
                                                                                    '_type': 'xsd:string'},
                                                                      'choice': {'_maxOccurs': 'unbounded',
                                                                                 '_minOccurs': '0',
                                                                                 'element': [{'_name': 'CrossProduct',
                                                                                              '_type': 'CrossProductType'},
                                                                                             {'_name': 'Tuples',
                                                                                              '_type': 'TuplesType'},
                                                                                             {'_name': 'Members',
                                                                                              '_type': 'MembersType'}]}}}}},
                            {'_name': 'CellData',
                             'sequence': {'element': {'_maxOccurs': 'unbounded',
                                                      '_minOccurs': '0',
                                                      '_name': 'Cell',
                                                      'complexType': {'attribute': {'_name': 'CellOrdinal',
                                                                                    '_type': 'xsd:unsignedInt',
                                                                                    '_use': 'required'},
                                                                      'sequence': {'_maxOccurs': 'unbounded',
                                                                                   'choice': {'element': [{'_name': 'Value'},
                                                                                                          {'_name': 'FmtValue',
                                                                                                           '_type': 'xsd:string'},
                                                                                                          {'_name': 'BackColor',
                                                                                                           '_type': 'xsd:unsignedInt'},
                                                                                                          {'_name': 'ForeColor',
                                                                                                           '_type': 'xsd:unsignedInt'},
                                                                                                          {'_name': 'FontName',
                                                                                                           '_type': 'xsd:string'},
                                                                                                          {'_name': 'FontSize',
                                                                                                           '_type': 'xsd:unsignedShort'},
                                                                                                          {'_name': 'FontFlags',
                                                                                                           '_type': 'xsd:unsignedInt'},
                                                                                                          {'_name': 'FormatString',
                                                                                                           '_type': 'xsd:string'},
                                                                                                          {'_name': 'NonEmptyBehavior',
                                                                                                           '_type': 'xsd:unsignedShort'},
                                                                                                          {'_name': 'SolveOrder',
                                                                                                           '_type': 'xsd:unsignedInt'},
                                                                                                          {'_name': 'Updateable',
                                                                                                           '_type': 'xsd:unsignedInt'},
                                                                                                          {'_name': 'Visible',
                                                                                                           '_type': 'xsd:unsignedInt'},
                                                                                                          {'_name': 'Expression',
                                                                                                           '_type': 'xsd:string'}]}}}}}}],
            'element': {'_name': 'root',
                        'complexType': {'sequence': {'_maxOccurs': 'unbounded',
                                                     'element': [{'_name': 'OlapInfo',
                                                                  '_type': 'OlapInfo'},
                                                                 {'_name': 'Axes',
                                                                  '_type': 'Axes'},
                                                                 {'_name': 'CellData',
                                                                  '_type': 'CellData'}]}}}}}
