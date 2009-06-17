#ifndef IOCOOM_PERFORMANCE_MODEL_H
#define IOCOOM_PERFORMANCE_MODEL_H

#include <vector>

#include "performance_model.h"

/*
  In-order core, out-of-order memory performance model.

  We use a simpe scoreboard to keep track of registers.

  We also keep a store buffer to short circuit loads.
 */
class IOCOOMPerformanceModel : public PerformanceModel
{
public:
   IOCOOMPerformanceModel();
   ~IOCOOMPerformanceModel();

   void outputSummary(std::ostream &os);

   UInt64 getCycleCount();

private:

   void handleInstruction(Instruction *instruction);

   UInt64 executeLoad(UInt64 occupancy, IntPtr addr);
   UInt64 executeStore(UInt64 occupancy, IntPtr addr);

   typedef std::vector<UInt64> Scoreboard;

   class ExecutionUnit
   {
   public:
      ExecutionUnit(unsigned int num_units);
      ~ExecutionUnit();

      UInt64 execute(UInt64 time, UInt64 occupancy);

   private:
      Scoreboard m_scoreboard;
   };

   class StoreBuffer
   {
   public:
      StoreBuffer(unsigned int num_entries);
      ~StoreBuffer();

      /*
        @return Time store finishes.
        @param time Time store starts.
        @param addr Address of store.
      */
      UInt64 executeStore(UInt64 time, UInt64 occupancy, IntPtr addr);

      /*
        @return True if addr is in store buffer at given time.
        @param time Time to check for addr.
        @param addr Address to check.
      */
      bool isAddressAvailable(UInt64 time, IntPtr addr);

   private:
      Scoreboard m_scoreboard;
      std::vector<IntPtr> m_addresses;
   };

   Scoreboard m_register_scoreboard;
   ExecutionUnit *m_load_unit;
   StoreBuffer *m_store_buffer;

   UInt64 m_instruction_count;
   UInt64 m_cycle_count;
};

#endif // IOCOOM_PERFORMANCE_MODEL_H
