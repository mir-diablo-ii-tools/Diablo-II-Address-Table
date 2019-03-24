# Diablo-II-Address-Table

A project that aims to collect Diablo II addresses into one place. The files containing the addresses are stored using tab-delimited values format.

## Supported Versions
These are the only versions that are supported in this address list. If you would like to see this project change its stance on a particular version, feel free to petition under Issues, or submit a Pull Request with the proper addresses.

- 1.00: The game as it was originally released.
- 1.03: The game as released in the original Battle Chest.
- 1.05B: The game at its most stable point before the release of LoD.
- 1.09D: The last version of the game before the big update.
- 1.10: The big update.
- 1.12A: Same as the 1.11B update, but with No-CD.
- 1.13C: The de-facto SlashDiablo version (as of 2019).
- 1.13D: The last version before the monolithic EXE.
- LoD 1.14C: The most stable monolithic EXE version before another code refactor.
- LoD 1.14D: The game after refactoring the code.

## Unsupported Versions
- Pre-1.05B: Unstable and not different enough to matter.
- 1.06, 1.06B: According to fearedbliss, has anti-dupe code that messes with single player.
- Pre-1.09D: Not popular versions.
- 1.11, 1.11B: The 1.12A patch is the same, but features No-CD.
- Classic 1.14A and above: Most players have LoD. 
- 1.14A, 1.14B: Glide usage bugs.

## Contributing
All contributions can be made using Pull Requests. The goal of using Pull Requests is to act as a system for documenting addresses and the repeatable methodology for finding them. You must validate every change you make and ensure that it is fully working. You must document the procedure for finding every address. This information will be used to review your Pull Request. If it found to be satisfactory, but not completely conformant, you may be asked to make appropriate changes. If you submit a Pull Request, you agree that you have full permission to submit the changes and that you agree to dedicate your changes to the Public Domain.

### Important questions to answer:
- What is the name of the address? This should be answered by the title of the Pull Request.
- Where can the address be found? This should be answered by the changes.
- What is the type of the data? This should be answered using standard C types and Diablo II structs. Do not use any Windows types unless there is an appropriate justification.
- If the changes are missing for certain Diablo II versions, why are they missing?
- If the address points to data:
  - What are the possible values?
  - What are some ingame ways to change this value? If you cannot answer this question, then how will changing this value affect the behavior of the game?
- If the address points to a function:
  - What are the inputs, the output, and their types? This should be answered using standard C types and Diablo II structs. Do not use any Windows types unless there is an appropriate justification.
  - What is the calling convention? You must enumerate the calling conventions for every version.
  - What are some examples of expected output, given some input? If the output is dependent on the state of the game, then provide a reasonable amount of information to get the game to this state.

### Your Pull Request may be rejected due to the following reasons:
- The documentation is incomplete or incorrect.
- The number of changes is too large.
- The individual changes are unrelated to each other.
- The address is useless, points to the stack or heap, or points to kernel space.
- The address documents void* (or aliases) types without proper justification.
- The address is a getter or setter function. It does not matter that the function can be located using an ordinal value. You should instead base your Pull Request around the encapsulated data.

## License
The project is dedicated to the public domain, as this is a compilation of reverse engineering and public information shared among modders.

## Special Thanks
- [Phrozen Keep](https://d2mods.info) - For providing tons of resources for Diablo II modding and being helpful.
- [SlashDiablo](https://reddit.com/r/slashdiablo) - For being an awesome community that got me interested in modding in the first place.
- Anyone else I failed to mention that played an instrumental role.
